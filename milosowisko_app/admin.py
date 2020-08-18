from django.contrib import admin
from .models import Zamowienie, ZamowioneDanie

# Register your models here.

class ZamowienieAdmin(admin.ModelAdmin):
    readonly_fields = ('data_losowania',)


admin.site.register(Zamowienie, ZamowienieAdmin)
admin.site.register(ZamowioneDanie)