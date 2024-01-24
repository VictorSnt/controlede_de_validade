from django.db import models


class Detalhe(models.Model):
    
    class Meta:
        db_table = 'detalhe'  
        managed = False 
        
    iddetalhe = models.CharField(max_length=40, primary_key=True)
    idproduto = models.CharField(max_length=40, null=True, blank=True)
    idcaracteristica = models.CharField(max_length=40, null=True, blank=True)
    dsdetalhe = models.CharField(max_length=50, null=True, blank=True)
    iddetgradeh = models.CharField(max_length=40, null=True, blank=True)
    iddetgradev = models.CharField(max_length=40, null=True, blank=True)
    vlprecocusto = models.FloatField(null=True, blank=True)
    vldesc1 = models.FloatField(null=True, blank=True)
    vldesc2 = models.FloatField(null=True, blank=True)
    tpdesc2 = models.CharField(max_length=1, null=True, blank=True)
    vlperipi = models.FloatField(null=True, blank=True)
    vlperfrete = models.FloatField(null=True, blank=True)
    vlpericms = models.FloatField(null=True, blank=True)
    vloutros = models.FloatField(null=True, blank=True)
    vlpermarkup = models.FloatField(null=True, blank=True)
    vlprecovenda = models.FloatField(null=True, blank=True)
    dsimagem = models.CharField(max_length=20, null=True, blank=True)
    qtestoque = models.FloatField(null=True, blank=True)
    qtestoque2 = models.FloatField(null=True, blank=True)
    qtexpminima = models.FloatField(null=True, blank=True)
    qtminima = models.FloatField(null=True, blank=True)
    qtmaxima = models.FloatField(null=True, blank=True)
    qtcritica = models.FloatField(null=True, blank=True)
    stpesado = models.CharField(max_length=1, null=True, blank=True)
    steditadesc = models.CharField(max_length=1, null=True, blank=True)
    stexp = models.CharField(max_length=1, null=True, blank=True)
    cdexterno = models.CharField(max_length=20, null=True, blank=True)
    tpclassifabcloja = models.CharField(max_length=1, null=True, blank=True)
    tpclassifabcrede = models.CharField(max_length=1, null=True, blank=True)
    percentvendaloja = models.FloatField(null=True, blank=True)
    percentvendarede = models.FloatField(null=True, blank=True)
    nrrankloja = models.IntegerField(null=True, blank=True)
    nrrankrede = models.IntegerField(null=True, blank=True)
    qtestoquecentral = models.IntegerField(null=True, blank=True)
    obs = models.TextField(null=True, blank=True)
    vlprecovendaant = models.FloatField(null=True, blank=True)
    dtaltvlprecovenda = models.DateTimeField(null=True, blank=True)
    statusalt = models.CharField(max_length=3, null=True, blank=True)
    pesoliquido = models.FloatField(null=True, blank=True)
    pesobruto = models.FloatField(null=True, blank=True)
    cdprincipal = models.CharField(max_length=20, null=True, blank=True)
    allucro = models.FloatField(null=True, blank=True)
    stlojavirtual = models.CharField(max_length=1, null=True, blank=True)
    qtembalagem = models.FloatField(null=True, blank=True)
    allucrodesejada = models.FloatField(null=True, blank=True)
    alcomissao = models.FloatField(null=True, blank=True)
    stbalanca = models.BooleanField(null=True, blank=True)
    stexpimg = models.CharField(max_length=1, null=True, blank=True)
    stcomissionado = models.BooleanField(null=True, blank=True)
    dtcadastro = models.DateTimeField(null=True, blank=True)
    vlvendaabc = models.FloatField(null=True, blank=True)
    qtvendaabc = models.FloatField(null=True, blank=True)
    vllucroabc = models.FloatField(null=True, blank=True)
    cdtratamentoespecial = models.CharField(max_length=3, null=True, blank=True)
    vlvendaabcrede = models.FloatField(null=True, blank=True)
    qtvendaabcrede = models.FloatField(null=True, blank=True)
    vllucroabcrede = models.FloatField(null=True, blank=True)
    dslocalizacao = models.CharField(max_length=50, null=True, blank=True)
    idfamilia = models.CharField(max_length=40, null=True, blank=True)
    stdesccomplementar = models.BooleanField(null=True, blank=True)
    dsdesccomplementar = models.CharField(max_length=200, null=True, blank=True)
    cdprodfiscal = models.CharField(max_length=9, null=True, blank=True)
    idunidadecompra = models.CharField(max_length=40, null=True, blank=True)
    stetiqgondola = models.BooleanField(null=True, blank=True)
    ststretchimagem = models.BooleanField(null=True, blank=True)
    sttrabalhaiss = models.BooleanField(null=True, blank=True)
    aliss = models.FloatField(null=True, blank=True)
    qtexpmaxima = models.FloatField(null=True, blank=True)
    dtaltvlprecocusto = models.DateTimeField(null=True, blank=True)
    idunidadetransf = models.CharField(max_length=40, null=True, blank=True)
    dtaltallucrodesejada = models.DateTimeField(null=True, blank=True)
    dtaltqtminima = models.DateTimeField(null=True, blank=True)
    dtaltqtcritica = models.DateTimeField(null=True, blank=True)
    dtaltnrrankloja = models.DateTimeField(null=True, blank=True)
    dtaltpercentvendaloja = models.DateTimeField(null=True, blank=True)
    dtalttpclassifabcloja = models.DateTimeField(null=True, blank=True)
    dtaltqtexpminima = models.DateTimeField(null=True, blank=True)
    dtaltqtexpmaxima = models.DateTimeField(null=True, blank=True)
    dtaltidunidadetransf = models.DateTimeField(null=True, blank=True)
    alipivenda = models.FloatField(null=True, blank=True)
    alroyalties = models.FloatField(null=True, blank=True)
    vlperpis = models.FloatField(null=True, blank=True)
    vlpercofins = models.FloatField(null=True, blank=True)
    stapurapiscofins = models.BooleanField(null=True, blank=True)
    cdnatoperservico = models.CharField(max_length=3, null=True, blank=True)
    tprecolhimentoiss = models.CharField(max_length=1, null=True, blank=True)
    stinativo = models.BooleanField(null=True, blank=True)
    naturezaoperacao = models.IntegerField(null=True, blank=True)
    cdsittribpisentrada = models.CharField(max_length=2, null=True, blank=True)
    cdsittribpis = models.CharField(max_length=2, null=True, blank=True)
    cdsittribcofinsentrada = models.CharField(max_length=2, null=True, blank=True)
    cdsittribcofins = models.CharField(max_length=2, null=True, blank=True)
    cdsituacaooperacao = models.CharField(max_length=3, null=True, blank=True)
    stmovimentaestoque = models.BooleanField(null=True, blank=True)
    cdtribmunicipio = models.CharField(max_length=20, null=True, blank=True)
    selofiscal = models.BooleanField(null=True, blank=True)
    cod_seloipi = models.CharField(max_length=6, null=True, blank=True)
    classeenquadraipi = models.CharField(max_length=5, null=True, blank=True)
    cdsituacaooperacaost = models.CharField(max_length=3, null=True, blank=True)
    origemmercadoria = models.CharField(max_length=1, null=True, blank=True)
    cdcombustivelanp = models.CharField(max_length=9, null=True, blank=True)
    alcargatributaria = models.FloatField(null=True, blank=True)
    alpiscompra = models.FloatField(null=True, blank=True)
    alcofinscompra = models.FloatField(null=True, blank=True)
    dtaltvloutros = models.DateTimeField(null=True, blank=True)
    fci = models.CharField(max_length=36, null=True, blank=True)
    stconciliacaouniversosped = models.IntegerField(null=True, blank=True)
    dtconciliacaouniversosped = models.DateTimeField(null=True, blank=True)
    percgasnaturalglp = models.FloatField(null=True, blank=True)
    alctfedimp = models.FloatField(null=True, blank=True)
    alctest = models.FloatField(null=True, blank=True)
    alctmun = models.FloatField(null=True, blank=True)
    alctfednac = models.FloatField(null=True, blank=True)
    pesoembalagem = models.FloatField(null=True, blank=True)
    fatorconvetiqueta = models.FloatField(null=True, blank=True)
    dsfatorconvetiqueta = models.CharField(max_length=20, null=True, blank=True)
    stdetalheativo = models.BooleanField(null=True, blank=True)
    cdnaturezareceita = models.CharField(max_length=3, null=True, blank=True)
    stcardapio = models.BooleanField(null=True, blank=True)
    percgasnaturalglpimp = models.FloatField(null=True, blank=True)
    percgaspetroleo = models.FloatField(null=True, blank=True)
    vlpartidaglp = models.FloatField(null=True, blank=True)
    ftconvunidtributaria = models.FloatField(null=True, blank=True)
    tpunidtributaria = models.CharField(max_length=6, null=True, blank=True)
    alfcp = models.FloatField(null=True, blank=True)
    qtvolumes = models.IntegerField(null=True, blank=True)
    alsubsttrib = models.FloatField(null=True, blank=True)
    percmva = models.FloatField(null=True, blank=True)
    codigonbs = models.CharField(max_length=9, null=True, blank=True)

    def __str__(self):
        return self.iddetalhe

