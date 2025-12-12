from django.shortcuts import render, redirect # pyright: ignore[reportMissingModuleSource]
from .models import Appointment, Servico, Horario
from datetime import date
from datetime import datetime

# Página inicial
def home(request):
    return render(request, 'booking/home.html')

# 1 - Seus Dados
def dados(request):
    if request.method == 'POST':
        request.session['nome'] = request.POST.get('nome')
        request.session['telefone'] = request.POST.get('telefone')
        return redirect('servicos')
    return render(request, 'booking/dados.html')

# 2 - Serviços
def servicos(request):
    from .models import Servico

    servicos = Servico.objects.all()

    if request.method == 'POST':
        services_ids = request.POST.getlist('servicos')
        request.session['servicos'] = services_ids
        return redirect('calendario')

    return render(request, 'booking/servicos.html', {'servicos': servicos})

# 3 - Calendário
def calendario(request):
    """
    Mostra os horários cadastrados no admin (model Horario).
    Remove os horários já ocupados na data selecionada.
    """
    selected_date = None
    horarios_qs = Horario.objects.all().order_by('hora')  # todos os horários do admin

    # Se veio via POST (form submit)
    if request.method == 'POST':
        # data e hora vêm do form
        selected_date = request.POST.get('data')
        hora_str = request.POST.get('hora')  # ex: "09:00" ou "09:00:00"

        # salvar data/hora na sessão para confirmar depois
        if selected_date:
            request.session['data'] = selected_date
        if hora_str:
            # guardar string; na finalização convertemos para TimeField/obj
            request.session['hora'] = hora_str
            return redirect('confirmar')

    # Se não é POST, podemos ter data via GET (para atualizar lista sem submeter)
    if request.GET.get('data'):
        selected_date = request.GET.get('data')
        request.session['data'] = selected_date

    # Filtrar horários ocupados só se data escolhida existe
    horarios_disponiveis = horarios_qs
    if selected_date:
        # buscar horários ocupados na data (Appointment.horario é TimeField)
        ocupados = Appointment.objects.filter(data=selected_date).values_list('horario', flat=True)
        # transformar em strings "HH:MM" para comparar com Horario.hora
        ocupados_str = [h.strftime("%H:%M") for h in ocupados]

        # Excluir da queryset os horarios cujo time em string esteja em ocupados_str
        horarios_disponiveis = horarios_qs.exclude(hora__in=ocupados).order_by('hora')

        # Observação: dependendo de como você compara, a exclusão por TimeField funciona diretamente
        # com horarios_qs.exclude(hora__in=ocupados) porque ambos são TimeField.
        # mantemos ocupados_str se precisar para lógica JS ou debug.

    # Passa a queryset (ou lista formatada) para o template
    return render(request, 'booking/calendario.html', {
        'horarios': horarios_disponiveis,
        'data_escolhida': selected_date
    })
# 4 - Confirmar
def confirmar(request):
    from .models import Servico

    ids = request.session.get('servicos', [])
    servicos_escolhidos = Servico.objects.filter(id__in=ids)

    total = sum(s.preco for s in servicos_escolhidos)

    contexto = {
        'nome': request.session.get('nome'),
        'telefone': request.session.get('telefone'),
        'data': request.session.get('data'),
        'hora': request.session.get('hora'),
        'servicos': servicos_escolhidos,
        'total': total,
    }

    return render(request, 'booking/confirmar.html', contexto)
# 5 - Finalizar
def finalizar(request):
    from .models import Servico, Appointment

    if request.method == 'POST':

        ids = request.session.get('servicos', [])
        servicos_escolhidos = Servico.objects.filter(id__in=ids)

        ag = Appointment.objects.create(
            nome=request.session.get('nome'),
            telefone=request.session.get('telefone'),
            data=request.session.get('data'),
            horario=request.session.get('hora'),
        )

        ag.servicos.set(servicos_escolhidos)

        total = sum(s.preco for s in servicos_escolhidos)

        contexto = {
            "nome": ag.nome,
            "telefone": ag.telefone,
            "data": ag.data,
            "hora": ag.horario,
            "servicos": servicos_escolhidos,
            "total": total
        }

        request.session.flush()

        return render(request, "booking/finalizado.html", contexto)

    return redirect("home")

# para cancelar
def cancelar(request, id):
    agendamento = Appointment.objects.get(id=id)

    # Se a data ainda não passou, pode remover
    if agendamento.data >= date.today():
        agendamento.delete()

    return redirect("meus_agendamentos")