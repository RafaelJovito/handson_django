# Generated by Django 2.1.7 on 2019-03-14 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('programa', models.CharField(max_length=255, verbose_name='Programa')),
                ('numero', models.CharField(max_length=50, verbose_name='Numero')),
                ('sigla', models.CharField(max_length=50, verbose_name='Sigla')),
                ('linkEdital', models.CharField(max_length=50, verbose_name='LinkEdital')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descricao')),
                ('ano', models.DateTimeField(auto_now=True, verbose_name='Ano')),
                ('periodo', models.DateTimeField(auto_now=True, verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'Edital',
                'verbose_name_plural': 'Edtitais',
            },
        ),
    ]