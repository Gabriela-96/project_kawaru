# Generated by Django 3.1.5 on 2021-05-11 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Metodo_Pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='perfiles')),
                ('identificacion', models.CharField(max_length=10, unique=True)),
                ('direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=15)),
                ('estado', models.BooleanField(default=True)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.persona')),
            ],
        ),
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=15)),
                ('precio_envio', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('usuario_compra', models.CharField(max_length=10)),
                ('usuario_venta', models.CharField(max_length=10)),
                ('metodo_paga', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.metodo_pago')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('iva', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.producto')),
            ],
        ),
    ]
