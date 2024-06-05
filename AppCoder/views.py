from django.shortcuts import render 
from django.http import HttpResponse
from .models import Curso
from .forms import CursoFormualrio

# Create your views here.
def curso(req, nombre, camada):

    nuevo_curso = Curso(nombre=nombre, camada=camada)
    nuevo_curso.save()

    return HttpResponse(f"""
        <p>Curso: {nuevo_curso.nombre} - Camada: {nuevo_curso.camada} creado!</p>
    """)

def lista_curso(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def inicio(req):

    return render(req, "inicio.html", {})

def cursos(req):

    return render(req, "cursos.html", {})

def profesores(req):

    return render (req,"profesores.html", {})

def estudiantes(req):

    return render (req,"estudiantes.html", {})

def entregables(req):

    return render (req,"entregables.html", {})

def curso_formulario(req):

    #print('method: ', req.method)
    #print('post: ', req.POST)

    if req.method == 'POST':

        miFormulario = CursoFormualrio(req.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            nuevo_curso = Curso(nombre=data['curso'], camada=data['camada'])
            nuevo_curso.save()

            return render(req, 'inicio.html', {"message": "Curso creado con exito"})
        
        else:
            
            return render(req, 'inicio.html', {"message": "Datos invalidos"})

    else:

        miFormulario = CursoFormualrio()

        return render(req, "curso_formulario.html", {"miFormulario": miFormulario})

def busqueda_camada(req):
    
    return render(req, "busqueda_camada.html", {})

def buscar(req):

    if req.GET["camada"]:
            
        camada = req.GET["camada"]

        curso = Curso.objects.filter(camada=camada) #(camada_icontrains=camada) busqueda parcial

        return render(req, 'resultadoBusqueda.html', {"curso": curso, "camada": camada})

    else:
        
        render(req, 'inicio.html', {"message": "No envio el dato de la camada"})