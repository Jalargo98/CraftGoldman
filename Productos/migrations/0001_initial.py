# Generated by Django 4.2.2 on 2024-04-03 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la categoria Principal', max_length=30)),
                ('descripcion', models.CharField(help_text='Descripcion de la categoria', max_length=40)),
            ],
            options={
                'db_table': 'categoria',
            },
        ),
        migrations.CreateModel(
            name='Subcategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre de la subcategoria Segundario', max_length=20)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.categoria')),
            ],
            options={
                'db_table': 'subcategoria',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del producto', max_length=30)),
                ('descripcion', models.TextField(help_text='Texto descriptivo del producto', max_length=500)),
                ('precio', models.DecimalField(decimal_places=2, help_text='Valor del producto antes de iva', max_digits=10)),
                ('porcentaje_iva', models.DecimalField(decimal_places=1, help_text='Porcentaje del iva ej = 16 - 19 ...', max_digits=3)),
                ('oferta', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('stock', models.IntegerField(help_text='Cantidad del producto en inventario')),
                ('estado', models.BooleanField(default=True)),
                ('subcategoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Productos.subcategoria')),
            ],
            options={
                'db_table': 'producto',
            },
        ),
    ]
