# Generated by Django 4.1.7 on 2023-05-31 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynakama', '0007_figura_fabricante_figura_medidas_manga_autor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='image',
        ),
        migrations.AddField(
            model_name='producto',
            name='image1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='image2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='image3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='image4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_descuento',
            field=models.IntegerField(default=0),
        ),
    ]