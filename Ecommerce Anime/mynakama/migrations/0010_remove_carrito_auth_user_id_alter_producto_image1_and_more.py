# Generated by Django 4.1.7 on 2023-06-01 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mynakama', '0009_figura_personaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrito',
            name='auth_user_id',
        ),
        migrations.AlterField(
            model_name='producto',
            name='image1',
            field=models.CharField(default='-', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='image2',
            field=models.CharField(default='-', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='image3',
            field=models.CharField(default='-', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='image4',
            field=models.CharField(default='-', max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id_orden', models.AutoField(primary_key=True, serialize=False)),
                ('auth_user_id', models.ForeignKey(db_column='auth_user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orden',
            },
        ),
        migrations.AddField(
            model_name='carrito',
            name='orden_id_orden',
            field=models.ForeignKey(db_column='orden_id_orden', null=True, on_delete=django.db.models.deletion.CASCADE, to='mynakama.orden'),
        ),
    ]
