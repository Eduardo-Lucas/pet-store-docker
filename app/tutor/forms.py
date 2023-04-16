from django import forms

from tutor.models import Tutor


class TutorForm(forms.ModelForm):

    class Meta:
        model = Tutor
        fields = '__all__'
        labels = {
            'nome': 'Nome do Tutor',
            'celular': 'Telefone Celular',
            'cpf': 'CPF',
            'rg': 'RG',
            'rua': 'Rua',
            'numero': 'Número',
            'complemento': 'Complemento',
            'bairro': 'Bairro',
            'cidade': 'Cidade',
            'uf': 'UF',
            'email': 'Email',
            'observacao': 'Observação',
        }