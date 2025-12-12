from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from .models import Appointment, Servico


# ADMIN DE SERVIÇOS
@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')
    search_fields = ('nome',)


# ADMIN DE AGENDAMENTO
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'listar_servicos', 'data', 'horario')
    list_filter = ('data',)
    search_fields = ('nome', 'telefone')

    def listar_servicos(self, obj):
        return ", ".join(s.nome for s in obj.servicos.all())

    listar_servicos.short_description = "Serviços"
