# vehicle/models.py
from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='нaзвание')
    description = models.TextField(verbose_name='onиcaние')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'
