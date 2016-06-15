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
	listaEscolar = (('sem','Não tem'),('fund','Fundamental'),('medio', 'Médio'),('super','Superior'),('pos','Pós-graduado'))
	listaOrigem=(('Cursilho','cursilho'),('Lado a Lado','lado a lado'),('Discipulado','discipulado'),('Transf outra comunidade','transf outra comunidade'),('Olímpiadas','olimpiadas'),('Outros','outros'))
	batizado = models.BooleanField(choices=((True,'Sim'),(False,'Nao')),blank=True)
	origem = models.CharField(max_length=6,choices=listaOrigem,blank=True)
	data_casamento = models.DateField(null=True,blank=True)
	conjuge = models.CharField(max_length=50,blank=True)
	profissao = models.CharField(max_length=50,blank=True)
	escolaridade = models.CharField(max_length=5,choices=listaEscolar,blank=True)
	pai = models.CharField(max_length=50,blank=True)
	mae = models.CharField(max_length=50,blank=True)
	data_nasc = models.DateField(null=True,blank=True)
	nome_comp = models.CharField(max_length=50)
	data_conf = models.DateField(null=True,blank=True)
	sexo = models.CharField(max_length=3, choices=listaGenero,blank=True)
	email = models.CharField(max_length=30,blank=True)
	endereco = models.ForeignKey(Endereco, related_name='endereco')
	data_batizado = models.DateField(null=True,blank=True)
	

class Telefone(models.Model):
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
	listaPeriodos = (('uma', 'uma vez'),('semanalmente','semanalmente'), ('quinzenal', 'quizenal'), ('mensal', 'mensal'))
	listaLocais = (('canaa', 'Canaã'),('betania','Catedral Betânia'), ('outros', 'Outros'))
	local = models.CharField(max_length=5,choices=listaLocais,blank=True)
	titulo = models.CharField(max_length=50)
	inicio = models.DateTimeField()
	fim = models.DateTimeField()
	peridiocidade = models.CharField(max_length=5,choices=listaPeriodos,blank=True)
	ser_divulgado = models.BooleanField()
	responsavel = models.ForeignKey(Membro, related_name='responsavel')
	secretario = models.ForeignKey(Secretario, related_name='secretario')

class Aconselhamento(models.Model):
	inicio = models.DateTimeField()
	fim = models.DateTimeField()
	sala = models.IntegerField(choices=((1,'sala 1'),(2, 'sala 2'),(3, 'sala 3'),(4, 'sala 4'),(5, 'sala 5')))
	secretario = models.ForeignKey(Secretario, related_name='agendou')
	lider = models.ForeignKey(Lider_religioso, related_name='lider_religioso')
	aconselhado = models.ForeignKey(Membro, related_name='aconselhado')
	
class Pertence_ministerio(models.Model):
	ministerio = models.IntegerField(choices=((1,'Cursilho'),(2, 'Mentoria de casais'),(3, 'Discipulado'),(4, 'Seminário de vida'),(5,'Olimpíadas')))
	pertencente = models.ForeignKey(Membro, related_name='cargo')
	#fez, trabalha ou lidera
	funcao = models.IntegerField(choices=((1,'fez'),(2, 'trabalha'),(3, 'lidera')))

class Mymodel(models.Model):
	photo = models.ImageField("somename",upload_to="images/")