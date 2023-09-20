from django.shortcuts import render, redirect
from .models import Colegio


# Create your views here.
def home(request):
    colegiosLista=Colegio.objects.all()
    
    return render(request, "gestionColegios.html", {"colegios": colegiosLista})

def registrarColegio(request):
    codigo=request.POST['codColegio']
    nombre=request.POST['nomColegio']
    colegio=Colegio.objects.create(
        codigo=codigo, nombre=nombre
    )
    return redirect('/')

def eliminarColegio(request, codigo):
    colegio=Colegio.objects.get(codigo=codigo)
    colegio.delete()
    
    return redirect('/')

def edicionColegio(request, codigo):
    colegio=Colegio.objects.get(codigo=codigo)
    return render(request, "edicionColegio.html", {"colegio":colegio})

def editarColegio(request):
    codigo=request.POST['codColegio']
    nombre=request.POST['nomColegio']
    colegio=Colegio.objects.get(codigo=codigo)
    colegio.nombre=nombre
    colegio.save()
    
    return redirect('/')