from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from .models import Servico, Horario, Appointment

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)

@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('hora',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'servico', 'data', 'horario')
    list_filter = ('data', 'servico')
    search_fields = ('nome', 'telefone')
