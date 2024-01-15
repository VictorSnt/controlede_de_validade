from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from .models import Validade, Produto

class ValidadeForm(forms.ModelForm):
    cdprincipal = forms.CharField(max_length=255, required=False, label='Cod produto',
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Validade
        fields = ['cdprincipal', 'dtvalidade', 'qtestoque']
        widgets = {
            'dtvalidade': forms.DateInput(attrs={'class': 'form-control'}),
            'qtestoque': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        cdprincipal = cleaned_data.get('cdprincipal')

        if cdprincipal:
            try:
                if len(cdprincipal) < 6:
                    cdprincipal = ("0" * (6 - len(cdprincipal)) + cdprincipal)
                produto_encontrado = Produto.objects.get(cdprincipal=cdprincipal)
                cleaned_data['produto'] = produto_encontrado.iddetalhe
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    f'O produto com o código "{cdprincipal}" não foi encontrado.')
        else:
            raise forms.ValidationError('O código do produto é obrigatório.')

        return cleaned_data

    def clean_dtvalidade(self):
        dtvalidade = self.cleaned_data.get('dtvalidade')

        if dtvalidade and dtvalidade < timezone.now().date():
            raise forms.ValidationError('A data de validade não pode ser no passado. e é obrigatória')
        return dtvalidade

    def clean_qtestoque(self):
        qtestoque = self.cleaned_data.get('qtestoque')
        if qtestoque and qtestoque <= 0:
            raise forms.ValidationError('A quantidade em estoque não pode ser negativa.')
        return qtestoque
