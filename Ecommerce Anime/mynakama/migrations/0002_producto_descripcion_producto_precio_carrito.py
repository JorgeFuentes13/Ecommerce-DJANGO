# Generated by Django 4.1.7 on 2023-05-31 03:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mynakama', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='carrito',
            fields=[
                ('id_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('auth_user_id', models.ForeignKey(db_column='auth_user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto_id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mynakama.producto')),
            ],
            options={
                'db_table': 'carrito',
            },
        ),
    ]
