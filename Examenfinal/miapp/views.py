from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

# Create your views here.
layout = """
    <h1>Universidad Nacional Tecnologica De Lima Sur</h1>
    <hr/>
    <ul>
        <li>
            <a href="/cursos">Cursos</a>
        </li>
        <li>
            <a href="/crearcurso">Crear curso</a>
        </li>
        <li>
            <a href="/carreras">Carreras</a>
        </li>
        <li>
            <a href="/crearcarrera">Crear Carrera</a>
        </li>
    </ul>
    <hr/>

"""
def index(request):
    mensaje ="""
        <h1>Listado de Cursos</h1>
    """
    return render(request,'index.html')

def crearcurso(request):
    mensaje ="""
    <h1>Agregar Curso</h1>
    """
    return render(request,'crearcurso.html')

def carreras(request):
    mensaje ="""
    <h1>Listado de Carreras</h1>
    """
    return render(request,'carreras.html')

def crearcarrera(request):
    mensaje ="""
    <h1>Agregar Carreras</h1>
    """
    return render(request,'crearcarrera.html')