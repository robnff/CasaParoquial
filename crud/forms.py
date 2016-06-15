from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from crud.models import Endereco
from crud.models import Membro
class AdicionarEndereco(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__' 
        # fields = ['numero','cep','bairro','complemento','cidade','estado','logradouro'] 

class AdicionarMembro(forms.ModelForm):
    class Meta:
        model = Membro
        fields = '__all__' 
        exclude = ('endereco',)
        # fields = ['nome_comp','data_nasc','data_casamento','batizado', 'conjuge','profissao','pai','mae','sexo','data_conf','email']
 