from django import forms
from .models import Motorista


class MotoristaForms(forms.ModelForm):
    
    class Meta:
        model = Motorista
        fields = ['nome', 'matricula', 'cnh', 'cpf', 'data_emissao', 'data_validade', 'categoria_cnh']
        
        widgets = {
            'nome': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'matricula': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'cnh': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'cpf': forms.TextInput(
                attrs={'class':'form-control'}
            ),
            'data_emissao': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type': 'date'
                       },
                format='%d/%m/%Y'
            ),
            'data_validade': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type': 'date'
                       },
                format='%d/%m/%Y'
            ),
            'categoria_cnh': forms.TextInput(
                attrs={'class':'form-control'}
            )
        }