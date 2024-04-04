"""
URL configuration for CraftGoldMan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('categoria/create/', categoriaC, name='categoriaC'),
    path('categoria/ver/', categoriaR, name='categoriaR'),
    path('categoria/update/<int:id_categoria>', categoriaU, name='categoriaU'),
    path('subcategoria/create/', subcategoriaC, name='subcategoriaC'),
    path('subcategoria/ver/', subcategoriaR, name='subcategoriaR'),
    path('subcategoria/update/<int:id_subcategoria>', subcategoriaU, name='subcategoriaU'),
    path('producto/create/', index, name='productoC'),
    path('producto/ver/', index, name='productoR'),
    path('producto/update/<int:id_producto>', index, name='productoU'),
]
