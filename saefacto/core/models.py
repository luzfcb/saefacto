from django.db import models

# Create your models here.


class AbstractPersonModel(models.Model):
    SEXO = (
        ('m', 'Macho'),
        ('f', 'Femea'),
        ('i', 'Que treco eh esse'),
    )

    nome = models.CharField(max_length=30)
    sexo = models.CharField(max_length=1, choices=SEXO)
    idade = models.DateField()

    class Meta:
        abstract = True


class Profile(AbstractPersonModel):
    pass


class Aluno(AbstractPersonModel):
    pass


class PerfilPermissoes(models.Model):
    pass

