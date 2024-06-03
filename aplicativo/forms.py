from django.forms import ModelForm
from aplicativo.models import Alunos

# Create the form class.isso vai levar as informacoes do imput para o banco de dados
class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ["nome_aluno", "idade_aluno", "curso_aluno"]
