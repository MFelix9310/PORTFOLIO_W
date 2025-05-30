# Generated by Django 5.2 on 2025-05-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_contact_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=200, verbose_name='Asunto')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('read', models.BooleanField(default=False, verbose_name='Leído')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
                'ordering': ['-created_at'],
            },
        ),
    ]
