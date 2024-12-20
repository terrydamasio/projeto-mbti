# Generated by Django 5.1.2 on 2024-11-25 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_mbti', '0002_cadastro_curso'),
        ('teste_mbti', '0005_respostas_chave_alter_respostas_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField()),
                ('comment', models.TextField(max_length=500)),
                ('chave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_mbti.cadastro')),
            ],
        ),
    ]
