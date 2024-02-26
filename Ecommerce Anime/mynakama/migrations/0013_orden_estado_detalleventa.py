# Generated by Django 4.1.7 on 2023-06-15 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mynakama', '0012_anime_producto_activo_alter_producto_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orden',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('completada', 'Completada')], default='Pendiente', max_length=20),
        ),
        migrations.CreateModel(
            name='DetalleVenta',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('total_venta', models.IntegerField(null=True)),
                ('orden_id_orden', models.ForeignKey(db_column='orden_id_orden', null=True, on_delete=django.db.models.deletion.CASCADE, to='mynakama.orden')),
            ],
            options={
                'db_table': 'detalle_venta',
            },
        ),
    ]