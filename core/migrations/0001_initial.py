# Generated by Django 4.2.2 on 2023-06-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('dt_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data Cadastro')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ['-dt_cadastro'],
            },
        ),
    ]
