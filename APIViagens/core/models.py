from datetime import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User

# Modelo de classificação de viagens
class Classification(models.Model):
    classificacao = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.classificacao

# Modelo de viagens
class Trip(models.Model):
    data_inicio = models.DateTimeField(default=datetime.now)
    data_fim = models.DateTimeField(default=datetime.now)
    classificacao = models.ForeignKey(Classification, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    nota = models.IntegerField(validators=[
                                        MaxValueValidator(5),
                                        MinValueValidator(1)
                                        ])

    class Meta:
        unique_together = ('data_inicio', 'data_fim', 'user_id',)

    def __str__(self):
        return str(self.id)
