from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class ZamowioneDanie(models.Model):
    czasdodania = models.DateTimeField(auto_now_add=True)
    zamowienione_danie = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.zamowienione_danie


class Zamowienie(models.Model):
    restauracja = models.CharField(max_length=100)
    data_losowania = models.DateTimeField(null=True, blank=True)
    losowanie_odbyte = models.BooleanField(default=False)
    wygrany = models.ForeignKey(User, on_delete=models.CASCADE)
    zamowienian = models.ManyToManyField(ZamowioneDanie)


    def __str__(self):
        return self.restauracja
