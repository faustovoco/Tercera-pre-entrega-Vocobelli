
from django.urls import path
from AppCoder.views import (curso, lista_curso, inicio, cursos, profesores, estudiantes, entregables, curso_formulario, busqueda_camada, buscar)

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_curso),
    path('', inicio, name='Inicio'), #sin nada es raiz, pasa a ser el index
    path('cursos/', cursos, name='Cursos'),
    path('profesores/', profesores, name='Profesores'),
    path('estudiantes/', estudiantes, name='Estudiantes'),
    path('entregables/', entregables, name='Entregables'),
    path('curso-formulario/', curso_formulario, name='CursoFormulario'),
    path('busqueda-camada/', busqueda_camada, name='BusquedaCamada'),
    path('buscar/', buscar, name='BuscarCurso'),

]

