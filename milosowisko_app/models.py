from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Zamowienie(models.Model):
    restauracja = models.CharField(max_length=100)
    czasdodania = models.DateTimeField(auto_now_add=True)
    zamowienione_danie = models.TextField(blank=True)
    data_losowania = models.DateTimeField(null=True, blank=True)
    losowanie_odbyte = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wygrany = models.BooleanField(default=False)

    
    

    def __str__(self):
        return self.title
