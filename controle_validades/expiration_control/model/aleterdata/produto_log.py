from django.db import models

class ProdutoLog(models.Model):
    
    class Meta:
        db_table = 'produtolog'  
        managed = False 
        
    idprodutolog = models.CharField(max_length=40, primary_key=True, default='nextval(\'wshop.produtolog_idprodutolog_seq\'::regclass)')
    idproduto = models.CharField(max_length=40)
    log = models.TextField()
    data = models.DateTimeField()
    stexp = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.idprodutolog} - {self.idproduto}"