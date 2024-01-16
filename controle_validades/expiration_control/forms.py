from django import forms
from django.utils import timezone
from .models import Validade, Produto
from .utils.database.alterdata_handler import build_connection


class ValidadeForm(forms.ModelForm):
    cdprincipal = forms.CharField(max_length=20, required=True)

    class Meta:
        model = Validade
        fields = ['cdprincipal', 'dtvalidade', 'qtestoque']

    def clean_cdprincipal(self):
        cdprincipal = self.cleaned_data.get('cdprincipal')
        if not cdprincipal:
            raise forms.ValidationError("Código interno do produto é obrigatório.")

        try:
            if len(cdprincipal) < 6:
                cdprincipal = '0'*(6 - len(cdprincipal)) + cdprincipal
            produto = Produto.objects.get(cdprincipal=cdprincipal)
        except Produto.DoesNotExist:
            alterdata_db = build_connection()
            with alterdata_db.connect():
                alterdata_produto = alterdata_db.get_product(cdprincipal)
            
            if not alterdata_produto:
                raise forms.ValidationError("Produto com este código interno não encontrado.")
            produto = Produto(**alterdata_produto[0])
            produto.save()
        return produto

    def clean_dtvalidade(self):
        dtvalidade = self.cleaned_data.get('dtvalidade')
        if not dtvalidade:
            raise forms.ValidationError("Data de validade é obrigatória.")

        if dtvalidade < timezone.now().date():
            raise forms.ValidationError("A data deve ser posterior a data de hoje.")

        return dtvalidade

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
