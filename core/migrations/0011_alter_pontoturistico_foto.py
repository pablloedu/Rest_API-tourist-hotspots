# Generated by Django 4.0 on 2021-12-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_pontoturistico_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/pontos_turisticos'),
        ),
    ]
