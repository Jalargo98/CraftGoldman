from django.shortcuts import render

# Create your views here.

def index(request):
  return render(request, 'index.html', {})
  pass

def autenticacion(request):
  return render(request, 'autenticacion.html', {})