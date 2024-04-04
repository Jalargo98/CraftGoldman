from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def tienda(request):
  productos = Producto.objects.filter(estado=True)
  context = {'productos': productos}
  return render(request, 'tienda.html', context)

def tienda_carrito(request):
  if request.user.is_authenticated:
    id_producto = request.GET.get('id_producto')
    product = Producto.objects.get(id=id_producto)
    cantiadd_producto = int(request.GET.get('cantidad'))

    # Obtener el carrito existente de la sesión, o crear uno nuevo si no existe
    carrito = request.session.get('carrito', {})

    if id_producto in carrito:
      # Si el producto ya está en el carrito, actualizar la cantidad
      carrito[id_producto]['cantidad'] += cantiadd_producto
      carrito[id_producto]['total'] = str(int(product.precio + (product.precio*(product.porcentaje_iva/100)) - (product.oferta * (product.precio/100)))*carrito[id_producto]['cantidad'])
    else:
      # Si el producto no está en el carrito, agregarlo al carrito
      carrito[id_producto] = {
        'cantidad': cantiadd_producto,
        'nombre': product.nombre,
        'precio': str(product.precio),
        'descripcion': product.descripcion,
        'imagen': product.imagen.url,
        'total': str(int(product.precio + (product.precio*(product.porcentaje_iva/100)) - (product.oferta * (product.precio/100)))*cantiadd_producto)
      }

    # Guardar el carrito actualizado en la sesión
    request.session['carrito'] = carrito

    print(request.session['carrito'])
    return JsonResponse({'message':'success'})
  else:
    return JsonResponse({'message':'No login found'})