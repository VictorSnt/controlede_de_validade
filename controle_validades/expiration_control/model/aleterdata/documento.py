from django.db import models

class Documento(models.Model):
    
    class Meta:
        db_table = 'documen'  
        managed = False 
        
    iddocumento = models.CharField(max_length=40, primary_key=True)
    idterminal = models.CharField(max_length=40, null=True, blank=True)
    idvendedor = models.CharField(max_length=40, null=True, blank=True)
    idpessoa = models.CharField(max_length=40, null=True, blank=True)
    cdempresa = models.CharField(max_length=15, null=True, blank=True)
    dtemissao = models.DateTimeField(null=True, blank=True)
    dtreferencia = models.DateTimeField(null=True, blank=True)
    hrreferencia = models.TimeField(null=True, blank=True)
    cdespecie = models.CharField(max_length=5, null=True, blank=True)
    cdseriesubserie = models.CharField(max_length=5, null=True, blank=True)
    nrdocumento = models.CharField(max_length=40, null=True, blank=True)
    stdocumentocancelado = models.CharField(max_length=1, null=True, blank=True)
    tpdocumento = models.CharField(max_length=1, null=True, blank=True)
    dsobservacao = models.CharField(max_length=255, null=True, blank=True)
    tp12 = models.CharField(max_length=1, null=True, blank=True)
    vltotal = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    aldesconto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vldesconto = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlacrescimo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    alacrescimo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    alcomissao = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    idprazo = models.CharField(max_length=40, null=True, blank=True)
    stexp = models.CharField(max_length=1, null=True, blank=True)
    cdexterno = models.CharField(max_length=20, null=True, blank=True)
    cdfiscal = models.CharField(max_length=6, null=True, blank=True)
    stfiscal = models.CharField(max_length=1, null=True, blank=True)
    tpciffob = models.CharField(max_length=1, null=True, blank=True)
    usuario = models.CharField(max_length=20, null=True, blank=True)
    vlsinal = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    idtransportador = models.CharField(max_length=40, null=True, blank=True)
    iddettransp = models.CharField(max_length=40, null=True, blank=True)
    iddocabertura = models.CharField(max_length=40, null=True, blank=True)
    calcicmsant = models.CharField(max_length=1, null=True, blank=True)
    icmsfonte = models.CharField(max_length=1, null=True, blank=True)
    vlrecolhido = models.CharField(max_length=1, null=True, blank=True)
    bssubst = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlsubst = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    bsicms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlicms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    stsomadespbasesubst = models.CharField(max_length=1, null=True, blank=True)
    stbasereduzidasubst = models.CharField(max_length=1, null=True, blank=True)
    stsomadespbaseicms = models.CharField(max_length=1, null=True, blank=True)
    stredbaseicms = models.CharField(max_length=1, null=True, blank=True)
    stdeduzicms = models.CharField(max_length=1, null=True, blank=True)
    stcalculasubst = models.CharField(max_length=1, null=True, blank=True)
    stcalculaicms = models.CharField(max_length=1, null=True, blank=True)
    vlseguro = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vloutros = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlfrete = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    idcontrolenf = models.CharField(max_length=40, null=True, blank=True)
    vlipi = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    bsipi = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    comissstabateicms = models.BooleanField(default=False)
    stgeracomflux = models.BooleanField(default=False)
    stipisomaicms = models.CharField(max_length=1, null=True, blank=True)
    stipisomast = models.CharField(max_length=1, null=True, blank=True)
    stdasomaipi = models.CharField(max_length=1, null=True, blank=True)
    stsomasubstanota = models.CharField(max_length=1, null=True, blank=True)
    stcalculaipi = models.CharField(max_length=1, null=True, blank=True)
    stdesconto = models.CharField(max_length=1, null=True, blank=True)
    stacrescimo = models.CharField(max_length=1, null=True, blank=True)
    idoperacao = models.CharField(max_length=40, null=True, blank=True)
    tpoperacao = models.CharField(max_length=1, null=True, blank=True)
    usuariodecancelamento = models.CharField(max_length=20, null=True, blank=True)
    stestorno = models.CharField(max_length=1, null=True, blank=True)
    idpessoamaster = models.CharField(max_length=40, null=True, blank=True)
    cdempvend = models.CharField(max_length=3, null=True, blank=True)
    usuorcedicao = models.CharField(max_length=20, null=True, blank=True)
    iddocestorno = models.CharField(max_length=40, null=True, blank=True)
    tpdevolucao = models.CharField(max_length=1, null=True, blank=True)
    vlttservicos = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlttiss = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlirretido = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    stcomplementoimposto = models.BooleanField(default=False)
    idpedido = models.CharField(max_length=40, null=True, blank=True)
    vlbonificacao = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    cdorcamento = models.CharField(max_length=15, null=True, blank=True)
    cd_atendimento = models.CharField(max_length=15, null=True, blank=True)
    cdmodelo = models.CharField(max_length=2, null=True, blank=True)
    bsicmsreduzida = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vldificms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    stvaloresalterados = models.BooleanField(default=False)
    vlconhecimento = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    dsobservacaomemo = models.TextField(null=True, blank=True)
    nrnsu = models.IntegerField(null=True, blank=True)
    dtnsu = models.DateTimeField(null=True, blank=True)
    vldiferimentoicms = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlpisret = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlcofinsret = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlinssret = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlirret = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlcsllret = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlbasecsrf = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlbaseinssret = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    vlbaseirrf = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    tpdocumentofatura = models.CharField(max_length=2, null=True, blank=True)
    emitentefatura = models.CharField(max_length=1, null=True, blank=True)
    desccomplementarfatura = models.CharField(max_length=50, null=True, blank=True)
    nrfatura = models.CharField(max_length=40, null=True, blank=True)
    stemissaopropria = models.CharField(max_length=1, null=True, blank=True)
    idsituacaodoc = models.CharField(max_length=40, null=True, blank=True)
    stpessoaicmssimples = models.BooleanField(default=False)
    vltotalnfe = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    stprodutoservico = models.BooleanField(default=False)
    stajusteicms = models.BooleanField(default=False)
    idnfe = models.CharField(max_length=40, null=True, blank=True)
    stabateicmsdesonerado = models.BooleanField(default=False)
    versao = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nrdocumento