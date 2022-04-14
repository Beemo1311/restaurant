from email.policy import default
from tabnanny import verbose
from typing import ChainMap
from django.db import models

from restaurant.settings import DEFAULT_AUTO_FIELD

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to = 'aboutUs/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Abiut Us'
        verbose_name_plural = 'Abiut Us'

class WhyChoiceUs(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'why choice us'
        verbose_name_plural = 'why choice us'

class Chef(models.Model):
    name = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    bio = models.TextField
    image = models.ImageField(upload_to = 'chef/')

    class Meta:
        verbose_name = 'Chef'
        verbose_name_plural = 'Chef'







