from distutils.command.upload import upload
from statistics import mode
from tabnanny import verbose
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=55)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Meals(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL, null=True)
    people = models.IntegerField()
    is_specionality = models.BooleanField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    preparation_time = models.IntegerField()
    image = models.ImageField(upload_to = 'meals/%Y/%m/%d/')
    slug = models.SlugField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = self.name
        return super(Meals, self).save(*args, *kwargs)

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

    def __str__(self):
        return self.name


