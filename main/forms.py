from django import forms
from main.models import Inscricao

class InscricaoForm(forms.ModelForm):
    class Meta:
        model=Inscricao
        fields = '__all__'
        
        widgets = {
            'minicursos': forms.CheckboxSelectMultiple(),
            'sexo': forms.RadioSelect(),
            'data_nascimento': forms.TimeInput(attrs={'type':'date'}),
        }