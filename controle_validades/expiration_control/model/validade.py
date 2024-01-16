from django.db import models
from .produto import Produto

class Validade(models.Model):
    idvalidade = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    dtvalidade = models.DateField(null=False)
    qtestoque = models.IntegerField(null=False)
    stativo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return f"{self.produto}: {self.dtvalidade}"
