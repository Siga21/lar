from django.shortcuts import render

from libros.models import autores, titulos, lectores

# Create your views here.
def home(request):
	return render(request, 'libros/home.html')
