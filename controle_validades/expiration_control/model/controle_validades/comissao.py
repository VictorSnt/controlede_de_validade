from django.db import models
from .product import Product


class Comissao(models.Model):
    idcomissao = models.AutoField(primary_key=True)
    iddocumento = models.CharField(max_length=20, unique=True)
    iddocumentoitem = models.CharField(max_length=20, unique=True)
    cdorcamento = models.CharField(max_length=20, unique=True)
    cdprincipal = models.ForeignKey(Product, on_delete=models.CASCADE)
    cdchamada = models.CharField(max_length=20, null=False)
    dsvendedor = models.CharField(max_length=80, null=False)
    vltotal = models.FloatField(null=False)
    ispaid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.dsvendedor}: {self.vltotal}"