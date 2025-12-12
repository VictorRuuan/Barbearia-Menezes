from django.db import models # pyright: ignore[reportMissingModuleSource]

class Servico(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.nome} - R$ {self.preco}"


class Horario(models.Model):
    hora = models.TimeField()

    def __str__(self):
        return self.hora.strftime("%H:%M")


class Appointment(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    servicos = models.ManyToManyField(Servico)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"{self.nome} - {self.servico.nome}"
