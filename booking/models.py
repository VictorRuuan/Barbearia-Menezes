from django.db import models

SERVICES = [
    ('Corte Simples', 'Corte Simples — R$35'),
    ('Degrade', 'Degradê — R$45'),
    ('Barba', 'Barba — R$30'),
    ('Sobrancelha', 'Sobrancelha — R$15'),
    ('Corte + Barba', 'Corte + Barba — R$65'),
    ('Pigmentacao', 'Pigmentação — R$50'),
]

class Appointment(models.Model):
    nome = models.CharField('Nome', max_length=120)
    telefone = models.CharField('Telefone', max_length=30)
    servico = models.CharField('Serviço', max_length=50, choices=[(s[0], s[0]) for s in SERVICES])
    data = models.DateField()
    horario = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} - {self.servico} - {self.data} {self.horario}"
