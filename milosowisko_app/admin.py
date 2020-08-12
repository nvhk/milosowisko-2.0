from django.contrib import admin
from .models import Zamowienie

# Register your models here.

class ZamowienieAdmin(admin.ModelAdmin):
    readonly_fields = ('czasdodania',)

admin.site.register(Zamowienie, ZamowienieAdmin)