from django.shortcuts import render


from libros.models import autores, titulos, lectores

# Create your views here.
def home(request):
	return render(request, 'libros/home.html')
	
def libros_index(request):
 	los_libros = titulos.objects.all()
	context = {'los_libros': los_libros }
	return render(request, 'libros/index.html', context)
