from django import forms

class CursoFormualrio(forms.Form):

    curso = forms.CharField()
    camada= forms.IntegerField()