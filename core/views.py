from django.shortcuts import render

# Create your views here.

# al definir las vistas apetir de funiones el parametro debe ser request y el nombre del template a renderizar
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def visit(request):
    return render(request, 'visit.html')

def contact(request):
    return render(request, 'contact.html')


def sample(request):
    return render(request, 'sample.html')


