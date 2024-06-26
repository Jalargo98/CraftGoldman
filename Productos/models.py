from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from uuid import uuid4

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=30,help_text="Nombre de la categoria Principal")
    descripcion = models.CharField(max_length=40,help_text="Descripcion de la categoria")
    
    def __str__(self) -> str:
        return f'{self.nombre}'
    class Meta:
        db_table = 'categoria'
        
        
class Subcategoria(models.Model):
    nombre = models.CharField(max_length=20,help_text="Nombre de la subcategoria Segundario")
    categoria = models.ForeignKey('Categoria',on_delete=models.SET_NULL,null=True)
    
    def __str__(self) -> str:
        return f'{self.nombre} {self.categoria}'
    class Meta:
        db_table = 'subcategoria'
    

class Producto(models.Model):
    nombre = models.CharField(max_length=30,help_text="Nombre del producto")
    descripcion = models.TextField(max_length=500,help_text="Texto descriptivo del producto")
    subcategoria = models.ForeignKey('Subcategoria',on_delete=models.SET_NULL,null=True)
    precio = models.DecimalField(max_digits=10,decimal_places=2,help_text="Valor del producto antes de iva")
    porcentaje_iva = models.DecimalField(max_digits=3,decimal_places=1,help_text="Porcentaje del iva ej = 16 - 19 ...")
    oferta = models.DecimalField(max_digits=4,decimal_places=2,null=True)
    stock = models.IntegerField(help_text="Cantidad del producto en inventario")
    imagen = models.ImageField()
    estado = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f'{self.nombre} "{self.stock}" "{self.subcategoria.nombre}"'
    class Meta:
        db_table = 'producto'
        
class CustomUser(AbstractUser):
    telefono = models.CharField(max_length=20, blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True, help_text='Specific permissions for this user.')