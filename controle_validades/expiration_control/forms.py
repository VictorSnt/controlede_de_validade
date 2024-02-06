from django import forms
from django.utils import timezone
from django.forms.models import model_to_dict
from .models import Validade, Product, Detalhe


class ValidadeForm(forms.ModelForm):
    cdprincipal = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Validade
        fields = ['cdprincipal', 'dtvalidade', 'qtestoque']
        widgets = {
            'dtvalidade': forms.DateInput(attrs={'class': 'form-control datepicker', 'type': 'date'}),
        }

    
    def __init__(self, *args, **kwargs):
        super(ValidadeForm, self).__init__(*args, **kwargs)
        self.fields['cdprincipal'].widget.attrs.update({'class': 'form-control'})
        self.fields['qtestoque'].widget.attrs.update({'class': 'form-control'})
        
    def clean_cdprincipal(self):
        cdprincipal = self.cleaned_data.get('cdprincipal')
        if not cdprincipal:
            raise forms.ValidationError("Código interno do produto é obrigatório.")

        try:
            if len(cdprincipal) < 6:
                cdprincipal = '0'*(6 - len(cdprincipal)) + cdprincipal
            produto = Product.objects.get(cdprincipal=cdprincipal)
        except Product.DoesNotExist:
            alterdata_produto = Detalhe.objects.using('alterdata').get(cdprincipal=cdprincipal)
            
            if not alterdata_produto:
                raise forms.ValidationError("Produto com este código interno não encontrado.")
            
            produto = Product(
                iddetalhe=alterdata_produto.iddetalhe, cdprincipal=alterdata_produto.cdprincipal,
                dsdetalhe=alterdata_produto.dsdetalhe
            )
            produto.save()
        return produto

    def clean_qtestoque(self):
        qtestoque = self.cleaned_data.get('qtestoque')
        if qtestoque is None or qtestoque <= 0:
            raise forms.ValidationError("A quantidade em estoque deve ser um número positivo.")

        return qtestoque

    def save(self, commit=True):
        
        produto = self.cleaned_data.get('cdprincipal')
        instance = Validade(
            produto=produto,
            dtvalidade=self.cleaned_data.get('dtvalidade'),
            qtestoque=self.cleaned_data.get('qtestoque'),
        )
        
        if commit:
            instance.save()
        
        return instance
