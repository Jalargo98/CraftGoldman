# Generated by Django 4.2.2 on 2024-04-04 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0004_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to=''),
        ),
    ]