# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aconselhamento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('inicio', models.DateTimeField()),
                ('fim', models.DateTimeField()),
                ('sala', models.IntegerField(verbose_name=[1, 2, 3, 4, 5])),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('cep', models.CharField(max_length=9)),
                ('bairro', models.CharField(max_length=25)),
                ('complemento', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=25)),
                ('estado', models.CharField(max_length=25)),
                ('logradouro', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('local', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('inicio', models.DateTimeField()),
                ('fim', models.DateTimeField()),
                ('ser_divulgado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Filho',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data_nasc', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lider_religioso',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('batizado', models.BooleanField(choices=[(True, 'Sim'), (False, 'Nao')])),
                ('origem', models.CharField(choices=[('cursilho','cursilho'),('lado','lado a lado'),('discipulado','discipulado'),('transf','transf outra comunidade'),('olimp','olimpiadas'),('outros','outros')], max_length=6)),
                ('data_casamento', models.DateField()),
                ('conjuge', models.CharField(max_length=50)),
                ('profissao', models.CharField(max_length=50)),
                ('pai', models.CharField(max_length=50)),
                ('mae', models.CharField(max_length=50)),
                ('data_nasc', models.DateField()),
                ('nome_comp', models.CharField(max_length=50)),
                ('data_conf', models.DateField()),
                ('sexo', models.CharField(choices=[('mas', 'masculino'), ('fem', 'feminino'), ('out', 'outro')], max_length=3)),
                ('email', models.CharField(max_length=30)),
                ('endereco', models.ForeignKey(related_name='endereco', to='crud.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Pertence_ministerio',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('ministerio', models.IntegerField(verbose_name=[1, 2, 3,4,5])),
                ('funcao', models.IntegerField(verbose_name=[1, 2, 3])),
                ('pertencente', models.ForeignKey(related_name='cargo', to='crud.Membro')),
            ],
        ),
        migrations.CreateModel(
            name='Secretario',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Telefones',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('dono', models.ForeignKey(related_name='dono', to='crud.Membro')),
            ],
        ),
        migrations.AddField(
            model_name='filho',
            name='genitor',
            field=models.ForeignKey(related_name='progenitor', to='crud.Membro'),
        ),
        migrations.AddField(
            model_name='evento',
            name='responsavel',
            field=models.ForeignKey(related_name='responsavel', to='crud.Membro'),
        ),
        migrations.AddField(
            model_name='evento',
            name='secretario',
            field=models.ForeignKey(related_name='marcou', to='crud.Secretario'),
        ),
        migrations.AddField(
            model_name='aconselhamento',
            name='aconselhado',
            field=models.ForeignKey(related_name='aconselhado', to='crud.Membro'),
        ),
        migrations.AddField(
            model_name='aconselhamento',
            name='lider',
            field=models.ForeignKey(related_name='lider_religioso', to='crud.Lider_religioso'),
        ),
        migrations.AddField(
            model_name='aconselhamento',
            name='secretario',
            field=models.ForeignKey(related_name='agendou', to='crud.Secretario'),
        ),
    ]
