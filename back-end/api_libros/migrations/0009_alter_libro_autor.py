# Generated by Django 5.0.7 on 2024-07-25 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_libros', '0008_alter_libro_autor_alter_libro_fecha_publicacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(max_length=500),
        ),
    ]
