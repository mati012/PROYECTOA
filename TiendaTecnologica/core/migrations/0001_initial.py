# Generated by Django 3.2.5 on 2021-07-01 09:50

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
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de categoría')),
                ('nombreCategoria', models.CharField(max_length=80, verbose_name='Nombre de la categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.IntegerField(primary_key=True, serialize=False, verbose_name='idProducto')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('precio', models.IntegerField(blank=True, null=True, verbose_name='Precio')),
                ('imagen', models.ImageField(default='sinfoto.jpg', upload_to='images/', verbose_name='Imagen')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.categoria')),
            ],
        ),
    ]