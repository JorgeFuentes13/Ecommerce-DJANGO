# Generated by Django 4.1.7 on 2023-05-31 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynakama', '0004_figura_manga_peluche'),
    ]

    operations = [
        migrations.AddField(
            model_name='manga',
            name='tomo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterModelTable(
            name='figura',
            table='Figura',
        ),
        migrations.AlterModelTable(
            name='manga',
            table='Manga',
        ),
        migrations.DeleteModel(
            name='Peluche',
        ),
    ]