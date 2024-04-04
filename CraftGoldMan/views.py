from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from Productos.models import CustomUser as User

# Create your views here.

def index(request):
  return render(request, 'index.html', {})
  pass

def autenticacion(request):
  if request.method == 'POST':
    user = authenticate(request,email=request.POST.get('email'),password=request.POST.get('password'))
    print(f'user == {user}')
    if user is not None:
            login(request, user)
            return redirect('index')
  return render(request, 'autenticacion.html', {})

def registro(request):
  if request.method == 'POST':
    try:
      user = User()
      user.username = request.POST.get('username')
      user.set_password(request.POST.get('password'))
      user.email = request.POST['email']
      user.first_name = request.POST['first_name']
      user.last_name = request.POST['last_name']
      user.telefono = request.POST['phone']
      user.save()
      messages.success(request,'El usuario se a creado con exito')
    except KeyError as e:
      messages.error(request, e.message)
    except Exception as e:
      messages.error(request, f'Ha ocurrido un error al crear el usuario: {str(e)}')
    return redirect('autenticacion')
  else:
    messages.error(request, f'No cuentas con permisos para ingresar a esta url')
    return redirect('autenticacion')

def mision(request):
  return render(request, 'mision.html', {})

def politicas(request):
  return render(request, 'politicas.html', {})