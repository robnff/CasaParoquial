from django.db import models

# Create your models here.

class Endereco(models.Model):
	numero = models.IntegerField()
	cep = models.CharField(max_length=9)
	bairro = models.CharField(max_length=25)
	complemento = models.CharField(max_length=50)
	cidade = models.CharField(max_length=25)
	estado = models.CharField(max_length=25)
	logradouro = models.CharField(max_length=25)


class Membro (models.Model):
	listaGenero = (('mas','masculino'),('fem','feminino'),('out', 'outro'))
	listaEscolar = (('fund','fundamental completo'),('medio', 'medio completo'),('super','superior completo'))

	#escolaridade = models.CharField(max_length=5, choices=listaGenero)
	batizado = models.BooleanField(choices=((True,'Sim'),(False,'Nao')))
	data_casamento = models.DateField()
	conjuge = models.CharField(max_length=50)
	profissao = models.CharField(max_length=50)
	#origem =
	pai = models.CharField(max_length=50)
	mae = models.CharField(max_length=50)
	data_nasc = models.DateField()
	nome_comp = models.CharField(max_length=50)
	data_conf = models.DateField()
	sexo = models.CharField(max_length=3, choices=listaGenero)
	email = models.CharField(max_length=30)
	endereco = models.ForeignKey(Endereco, related_name='endereco')
	

class Telefones(models.Model):
	numero = models.CharField(max_length=15)
	dono = models.ForeignKey(Membro, related_name='dono')

class Lider_religioso(models.Model):
	nome = models.CharField(max_length=50)

class Secretario(models.Model):
	nome = models.CharField(max_length=50)

class Filho(models.Model):
	nome = models.CharField(max_length=50)
	data_nasc = models.DateField()
	genitor = models.ForeignKey(Membro, related_name='progenitor')

class Evento(models.Model):
	local = models.CharField(max_length=50)
	titulo = models.CharField(max_length=50)
	inicio = models.DateTimeField()
	fim = models.DateTimeField()
	#periodicidade =
	ser_divulgado = models.BooleanField()
	responsavel = models.ForeignKey(Membro, related_name='responsavel')
	secretario = models.ForeignKey(Secretario, related_name='marcou')

class Aconselhamento(models.Model):
	inicio = models.DateTimeField()
	fim = models.DateTimeField()
	sala = models.IntegerField([1,2,3,4,5])
	secretario = models.ForeignKey(Secretario, related_name='agendou')
	lider = models.ForeignKey(Lider_religioso, related_name='lider_religioso')
	aconselhado = models.ForeignKey(Membro, related_name='aconselhado')

class Pertence_ministerio(models.Model):
	ministerio = models.CharField(max_length=50)
	pertencente = models.ForeignKey(Membro, related_name='cargo')
	#fez, trabalha ou lidera
	funcao = models.CharField(max_length=50)

