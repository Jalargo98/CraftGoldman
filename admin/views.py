from django.shortcuts import render, redirect
from Productos.models import Categoria,Subcategoria
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
  
  

def subcategoriaC(request):
  if request.method == 'POST':
    try:
      cat = Subcategoria()
      cat.nombre = request.POST.get('nombre')
      cat.categoria = Categoria.objects.get(id=request.POST.get('categoria'))
      print(cat)
      cat.save()
      return redirect('admin:subcategoriaR')
    except KeyError as e:
      print(e)
      return redirect('admin:subcategoriaC')
    except Exception as e:
      print(e)
      return redirect('admin:subcategoriaC')
  else:
    cat = Categoria.objects.all()
    context = {'categorias': cat}
    return render(request,'admin/subcategoriaC.html',context)

def subcategoriaR(request):
  cat = Subcategoria.objects.all()
  context = {'subcategorias':cat}
  return render(request,'admin/subcategoriaR.html',context)

def subcategoriaU(request,id_subcategoria):
  try:
    subcat = Subcategoria.objects.get(id=id_subcategoria)
    cat = Categoria.objects.all()
  except ObjectDoesNotExist:
    return redirect('admin:subcategoriaR')
  if request.method == "POST":
    subcat.nombre = request.POST.get('nombre')
    subcat.categoria = Categoria.objects.get(id=request.POST.get('categoria'))
    subcat.save()
    return redirect('admin:subcategoriaR')
  else:
    context = {'categorias':cat,'subcategoria':subcat}
    return render(request,'admin/subcategoriaC.html',context)