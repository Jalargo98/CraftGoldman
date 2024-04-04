from django.shortcuts import render, redirect
from Productos.models import Categoria,Subcategoria,Producto
from django.core.exceptions import ObjectDoesNotExist
from .forms import FormProducto
from .decortadores import only_admin_access

# Create your views here.
@only_admin_access
def index(request):
  return render(request,'admin/index.html',{})
@only_admin_access
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
@only_admin_access
def categoriaR(request):
  cat = Categoria.objects.all()
  context = {'categorias':cat}
  return render(request,'admin/categoriaR.html',context)
@only_admin_access
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
  
  
@only_admin_access
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
@only_admin_access
def subcategoriaR(request):
  cat = Subcategoria.objects.all()
  context = {'subcategorias':cat}
  return render(request,'admin/subcategoriaR.html',context)
@only_admin_access
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
  
@only_admin_access
def productoC(request):
    if request.method == 'POST':
      form = FormProducto(request.POST, request.FILES)
      if form.is_valid():
        form.save()
        return redirect('admin:productoR')
      else:
        print(form.errors)
        subcat = Subcategoria.objects.all()
        context = {'form': form, 'subcategorias': subcat}
        return render(request, 'admin/productoC.html', context)
    else:
      subcat = Subcategoria.objects.all()
      context = {'subcategorias': subcat}
      return render(request, 'admin/productoC.html', context)
@only_admin_access
def productoR(request):
  prod = Producto.objects.all()
  context = {'productos':prod}
  return render(request,'admin/productoR.html',context)
@only_admin_access
def productoU(request,id_producto):
  try:
    producto = Producto.objects.get(id=id_producto)
    subcat = Subcategoria.objects.all()
    form = FormProducto(request.POST,request.FILES, instance=producto)
  except ObjectDoesNotExist:
    return redirect('admin:productoR')
  if request.method == "POST":
    if form.is_valid():
      form.save()
      return redirect('admin:productoR')
    else:
      print(form.errors)
      subcat = Subcategoria.objects.all()
      context = {'form': form, 'subcategorias': subcat}
      return render(request, 'admin/productoC.html', context)
  else:
    context = {'form': form,'producto':producto,'subcategorias':subcat}
    return render(request,'admin/productoC.html',context)