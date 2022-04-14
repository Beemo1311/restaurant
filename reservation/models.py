from operator import mod
from tabnanny import verbose
from django.db import models
from django.forms import TimeField

class Reservation(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.BigIntegerField()
    number_of_number = models.IntegerField()
    Date = models.DateField()
    time = TimeField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

