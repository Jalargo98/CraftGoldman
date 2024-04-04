from django.shortcuts import render, redirect
from Productos.models import Categoria
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
  return render(request,'admin/index.html',{})

def categoriaC(request):
  if request.method == 'POST':
    try:
      cat = Categoria()
      cat.nombre = request.POST.get('nombre')
      cat.descripcion = request.POST.get('descripcion')
      print(cat)
      cat.save()
      return redirect('admin:categoriaR')
    except KeyError as e:
      print(e)
      return redirect('admin:categoriaC')
    except Exception as e:
      print(e)
  return render(request,'admin/categoriaC.html',{})

def categoriaR(request):
  cat = Categoria.objects.all()
  context = {'categorias':cat}
  return render(request,'admin/categoriaR.html',context)

def categoriaU(request,id_categoria):
  try:
    cat = Categoria.objects.get(id=id_categoria)
  except ObjectDoesNotExist:
    return redirect('admin:categoriaR')
  if request.method == "POST":
    cat.nombre = request.POST.get('nombre')
    cat.descripcion = request.POST.get('descripcion')
    cat.save()
    return redirect('admin:categoriaR')
  else:
    context = {'categoria':cat}
    return render(request,'admin/categoriaC.html',context)