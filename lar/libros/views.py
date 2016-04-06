from django.shortcuts import render
from django.views.generic import ListView, DetailView
from libros.models import autores, titulos, lectores

# Create your views here.
def home(request):
	return render(request, 'libros/home.html')

class ListaTitulos(ListView):
    queryset = titulos.objects.order_by('-fecha')
    context_object_name = 'titulos'
    paginate_by = 8

class DetalleTitulos(DetailView):
    model = titulos

