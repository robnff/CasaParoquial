from django.shortcuts import render
from casaParoquial import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.
from .forms import AdicionarEndereco
from .forms import AdicionarMembro
from crud.models import Endereco
from crud.models import Membro, Secretario, Lider_religioso, Aconselhamento, Evento
from django.shortcuts import get_object_or_404
def home(request):
    if request.method == 'POST':
        username = request.POST['login']
        password = request.POST['senha']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {})
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


def cadastrar_membro(request):

    if request.method == 'POST':
        # membro
        nome = request.POST['nome']
        data_nascimento = request.POST['data_nascimento']
        sexo = request.POST['sexo']
        # origem = request.POST['origem']
        email = request.POST['email']
        profissao = request.POST['profissao']
        escolaridade = request.POST.get('escolaridade')
        batizado = request.POST.get('batizado')
        if batizado == None:
            batizado = False
        else:
            batizado = True    
        
        print(batizado)
        data_batismo = request.POST['data_batismo']
        data_confirmacao = request.POST['data_confirmacao']
        nome_conjuge = request.POST['nome_conjuge']
        nome_pai = request.POST['nome_pai']
        nome_mae = request.POST['nome_mae']
        data_casamento = request.POST.get('data_casamento')
        origem = request.POST.get('origem')
        # endereco
        print(origem)
        logradouro = request.POST['logradouro']
        bairro = request.POST['bairro']
        numero = request.POST['endereco_num']
        cep = request.POST['cep']
        complemento = request.POST['complemento']
        estado = request.POST['estado']
        cidade = request.POST['cidade']
        
        try:
            endereco =  Endereco.objects.get(cep=cep, logradouro=logradouro, numero=numero)
            # if it's a OneToOne field, you can do:
            # profile = request.user.myprofile
        except Endereco.DoesNotExist:
            endereco = None
            # other code that handles missin
            
        if endereco == None:
            # cria primeiro o endereco
            new_endereco = Endereco.objects.create(
                numero=numero,
                cep = cep,
                bairro = bairro,
                complemento = complemento,
                cidade = cidade,
                estado = estado,
                logradouro = logradouro
            )
        new_membro = Membro.objects.create(
            batizado = batizado,
            origem = origem,
            data_casamento = data_casamento,
            conjuge = nome_conjuge,
            profissao = profissao,
            pai = nome_pai,
            mae = nome_pai,
            data_nasc = data_nascimento,
            nome_comp = nome,
            data_conf = data_confirmacao,
            sexo = sexo,
            email = email,
            escolaridade = escolaridade,
            endereco = Endereco.objects.get(cep=cep, logradouro=logradouro, numero=numero)
        )
        
        return render(request, 'cadastrar_membro.html', {})

    else:
        return render(request, 'cadastrar_membro.html')
   
def cadastrar_aconselhamento(request):
    membros  = Membro.objects.all()
    secretarios = Secretario.objects.all()
    lideres = Lider_religioso.objects.all()
    if request.method == 'POST':
        aconselhado =  get_object_or_404(Membro, pk=request.POST.get('aconselhado'))
        lider =  get_object_or_404(Lider_religioso, pk=request.POST.get('lider'))
        secretario = get_object_or_404(Secretario, pk=request.POST.get('secretario'))
        sala = request.POST['sala']
        data_inicio = request.POST['data_inicio']
        data_fim = request.POST['data_fim']
        print(aconselhado)
        print(lider)
        print(secretario)
        new_aconselhamento = Aconselhamento.objects.create(
            inicio = data_inicio,
            fim = data_fim, 
            sala = sala, 
            secretario = secretario, 
            lider = lider, 
            aconselhado = aconselhado
        )
        return render(request, 'cadastrar_aconselhamento.html', {'membros':membros, 'secretarios':secretarios, 'lideres': lideres})
    else:
        return render(request, 'cadastrar_aconselhamento.html', {'membros':membros, 'secretarios':secretarios, 'lideres': lideres})
def cadastrar_evento(request):
    membros  = Membro.objects.all()
    secretarios = Secretario.objects.all()
    if request.method == 'POST':
        secretario = get_object_or_404(Secretario, pk=request.POST.get('secretario'))
        responsavel =  get_object_or_404(Membro, pk=request.POST.get('responsavel'))
        data_inicio = request.POST['inicio']
        data_fim = request.POST['fim']
        peridiocidade = request.POST.get('peridiocidade')
        divulgado = request.POST.get('divulgado')
        if divulgado == None:
            divulgado = False
        else:
            divulgado = True
        local = request.POST.get('local') 
        titulo = request.POST['titulo']
        
        new_evento = Evento.objects.create(
            local = local,
            titulo = titulo,
            inicio = data_inicio,
            fim = data_fim,
            peridiocidade = peridiocidade,
            ser_divulgado = divulgado,
            responsavel = responsavel,
            secretario = secretario
        )
    return render(request, 'cadastrar_evento.html', {'membros':membros, 'secretarios':secretarios})

def envia_email(request):
    #send_mail(subject, message, from_email, to_list, fail_silently=True)
    subject = 'acho que está funcionando!'
    message = 'uma funcionalidade a menos!uhuuul!'
    from_me = settings.EMAIL_HOST_USER
    from_password = settings.EMAIL_HOST_PASSWORD
    to_list = [settings.EMAIL_HOST_USER]

    send_mail(subject, message, from_email=from_me, recipient_list=to_list, auth_user=from_me, auth_password=from_password, fail_silently=True)
    return render(request, 'index.html',{})

def login_user1(request):
    usuario = User.objects.create_user('usuario1', 'lennon@thebeatles.com', 'senha1')
    usuario.save()

    return render(request, 'index.html', {})

def login_user2(request):
    usuario = User.objects.create_user('usuario2', 'lennon@thebeatles.com', 'senha2')
    usuario.save()

    return render(request, 'index.html', {})

def consulta_membro(request):
    if request.method == 'POST':
        #exibir lista
        partenome = request.POST['nome']
        membros =  Membro.objects.filter(nome_comp__contains=partenome)
        data_to_plot={}
        if(len(membros)==0):
            return render(request, 'membro_nao_existe.html', {})
        else:
            #for i in range(len(Membro)):
            print('MEMBROS ',membros)
        #falta passar a lista pra uma pag e exibir la, mas ta pegando ela pelo menos :) 
    else:
        return render(request, 'consultar_membro.html', {})

def consultar_evento(request):
    if request.method == 'POST':
        #exibir lista
        evento_inicio = request.POST['inicio']
        eventos =  Evento.objects.filter(inicio=evento_inicio)
        if(len(eventos)==0):
            return render(request, 'evento_nao_existe.html', {})
        else:
            print('eventos ',eventos)
        #falta passar a lista pra uma pag e exibir la, mas ta pegando ela pelo menos :) 
    else:
        return render(request, 'consultar_evento.html', {})

def consultar_aconselhamento(request):
    if request.method == 'POST':
        #exibir lista
        aconselhamento_inicio = request.POST['inicio']
        aconselhamentos = Aconselhamento.objects.filter(inicio=aconselhamento_inicio)
        if(len(aconselhamentos)==0):
            return render(request, 'aconselhamento_nao_encontrado.html', {})
        else:
            print('aconselhamentos ',aconselhamentos)
        #falta passar a lista pra uma pag e exibir la, mas ta pegando ela pelo menos :) 
    else:
        return render(request, 'consultar_aconselhamento.html', {})