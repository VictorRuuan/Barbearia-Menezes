from django.shortcuts import render, redirect # pyright: ignore[reportMissingModuleSource]
from .models import Appointment, Servico, Horario

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
    servicos = Servico.objects.all()

    if request.method == 'POST':
        request.session['servico'] = request.POST.get('servico')
        return redirect('calendario')

    return render(request, 'booking/servicos.html', {'servicos': servicos})

# 3 - Calendário
def calendario(request):
    horarios = Horario.objects.all()

    if request.method == 'POST':
        request.session['data'] = request.POST.get('data')
        request.session['hora'] = request.POST.get('hora')
        return redirect('confirmar')

    return render(request, 'booking/calendario.html', {'horarios': horarios})

# 4 - Confirmar
def confirmar(request):
    contexto = {
        'nome': request.session.get('nome'),
        'telefone': request.session.get('telefone'),
        'servico': request.session.get('servico'),
        'data': request.session.get('data'),
        'hora': request.session.get('hora'),
    }
    return render(request, 'booking/confirmar.html', contexto)

# 5 - Finalizar
def finalizar(request):
    if request.method == 'POST':

        nome = request.session.get('nome')
        telefone = request.session.get('telefone')
        servico_nome = request.session.get('servico')
        data = request.session.get('data')
        hora = request.session.get('hora')

        servico_obj = Servico.objects.filter(nome=servico_nome).first()
        preco = servico_obj.preco if servico_obj else 0

        Appointment.objects.create(
            nome=nome,
            telefone=telefone,
            servico=servico_nome,
            data=data,
            horario=hora,
        )

        contexto = {
            "nome": nome,
            "telefone": telefone,
            "servico": servico_nome,
            "data": data,
            "hora": hora,
            "preco": preco,
        }

        for k in ('nome','telefone','servico','data','hora'):
            request.session.pop(k, None)

        return render(request, 'booking/finalizado.html', contexto)

    return redirect('home')
