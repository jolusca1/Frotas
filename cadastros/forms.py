from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nome', 'cpfCnpj', 'tipo']
        
    def save(self, commit=True):
        cliente = super().save(commit=False)
        
        if commit:
            cliente.save()
        return cliente