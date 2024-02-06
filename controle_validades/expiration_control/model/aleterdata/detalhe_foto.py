from django.db import models
from .detalhe import Detalhe

class DetalheFoto(models.Model):
    
    class Meta:
        db_table = 'detalhefoto'
        managed = False
        
    iddetalhefoto = models.CharField(max_length=40, primary_key=True)
    iddetalhe = models.ForeignKey(Detalhe, related_name='detalhefoto', on_delete=models.DO_NOTHING)
    dsfoto = models.CharField(max_length=50, null=True, blank=True)
    stprincipal = models.BooleanField(null=True, blank=True)
    stlojavirtual = models.BooleanField(null=True, blank=True)
    stexp = models.CharField(max_length=1, null=True, blank=True)
    stexplojavirtual = models.CharField(max_length=1, null=True, blank=True)
    foto = models.BinaryField(null=True, blank=True)
    miniatura = models.BinaryField(null=True, blank=True)
    stautomatica = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.iddetalhefoto

    
