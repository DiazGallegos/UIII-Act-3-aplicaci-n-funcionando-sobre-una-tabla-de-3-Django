from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipo

def inicio_futbol(request):
    return render(request, 'inicio.html')

def agregar_equipo(request):
    if request.method == 'POST':
        Equipo.objects.create(
            nombre=request.POST['nombre'],
            ciudad=request.POST['ciudad'],
            pais=request.POST['pais'],
            fundacion=request.POST['fundacion'],
            estadio=request.POST['estadio'],
            entrenador=request.POST['entrenador'],
            colores=request.POST['colores']
        )
        return redirect('ver_equipos')
    return render(request, 'equipo/agregar_equipo.html')

def ver_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'equipo/ver_equipos.html', {'equipos': equipos})

def actualizar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    return render(request, 'equipo/actualizar_equipo.html', {'equipo': equipo})

def realizar_actualizacion_equipo(request, id):
    if request.method == 'POST':
        equipo = get_object_or_404(Equipo, id=id)
        equipo.nombre = request.POST['nombre']
        equipo.ciudad = request.POST['ciudad']
        equipo.pais = request.POST['pais']
        equipo.fundacion = request.POST['fundacion']
        equipo.estadio = request.POST['estadio']
        equipo.entrenador = request.POST['entrenador']
        equipo.colores = request.POST['colores']
        equipo.save()
        return redirect('ver_equipos')
    return redirect('ver_equipos')

def borrar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    return render(request, 'equipo/borrar_equipo.html', {'equipo': equipo})

def realizar_borrado_equipo(request, id):
    if request.method == 'POST':
        equipo = get_object_or_404(Equipo, id=id)
        equipo.delete()
        return redirect('ver_equipos')
    return redirect('ver_equipos')