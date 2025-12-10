from django.shortcuts import render, redirect
from .models import Appointment

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
    if request.method == 'POST':
        request.session['servico'] = request.POST.get('servico')
        return redirect('calendario')
    return render(request, 'booking/servicos.html')

# 3 - Calendário
def calendario(request):
    if request.method == 'POST':
        request.session['data'] = request.POST.get('data')
        request.session['hora'] = request.POST.get('hora')
        return redirect('confirmar')
    return render(request, 'booking/calendario.html')

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

# Finalizar (salvar no banco)
def finalizar(request):
    if request.method == 'POST':
        Appointment.objects.create(
            nome=request.session.get('nome'),
            telefone=request.session.get('telefone'),
            servico=request.session.get('servico'),
            data=request.session.get('data'),
            horario=request.session.get('hora')
        )
        # limpar sessão
        for key in ('nome','telefone','servico','data','hora'):
            request.session.pop(key, None)
        return render(request, 'booking/finalizado.html')

    return redirect('home')
