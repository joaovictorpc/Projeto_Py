from django.forms import ModelForm
 
from teste.models import Aluno
 
 
class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'