from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone', 'servico', 'data', 'horario', 'created_at')
    list_filter = ('servico', 'data')
    search_fields = ('nome', 'telefone')
