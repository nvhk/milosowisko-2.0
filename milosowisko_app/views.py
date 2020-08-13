from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Zamowienie

# Create your views here.

def rejestracja(request):
    
    if request.method == 'GET':
        # Wyswietl Strone
        return render(request, 'milosowisko_app/rejestracja.html')

    else:
        # Zrob usera

        #sprawdz hasla
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                #
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1']) #dodaj haslo
                user.save() # zapisz usera do bazy
                login(request, user) #zaloguj sie jako ten user
                return redirect('lista_zamowienia')

            #przechwyc czy user juz istnieje    
            except IntegrityError:
                return render(request, 'milosowisko_app/rejestracja.html', {'error':'Taki uzytkownik juz istnieje'})
            
        else:
            return render(request, 'milosowisko_app/rejestracja.html', {'error':'Hasła sie nie zgadzają'})



@login_required
def lista_zamowienia(request):

    lista = Zamowienie.objects.all()  #wszytkie
    # lista = Zamowienie.objects.filter(user=request.user, data_losowania__isnull=True)
    # lista = Zamowienie.objects.filter(data_losowania__isnull=True)
    return render(request, 'milosowisko_app/lista_zamowienia.html', {'lista':lista})


@login_required
def wyloguj(request):
    if request.method == 'POST':
        logout(request)
        return redirect('rejestracja')



def logowanie(request):
    if request.method == 'GET':
        # Wyswietl Strone z logowaniem
        return render(request, 'milosowisko_app/login.html')
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'] )

        if user is None:
            return render(request, 'milosowisko_app/login.html', {'error':'złe hasło lub użytnik' })
        
        else:
            login(request, user)
            return redirect('lista_zamowienia')