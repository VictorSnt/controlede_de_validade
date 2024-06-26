# Generated by Django 4.0 on 2024-01-30 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expiration_control', '0006_documentoitem_produtolog'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltedataDocs',
            fields=[
                ('iddocumento', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('idterminal', models.CharField(blank=True, max_length=40, null=True)),
                ('idvendedor', models.CharField(blank=True, max_length=40, null=True)),
                ('idpessoa', models.CharField(blank=True, max_length=40, null=True)),
                ('cdempresa', models.CharField(blank=True, max_length=15, null=True)),
                ('dtemissao', models.DateField(blank=True, null=True)),
                ('dtreferencia', models.DateField(blank=True, null=True)),
                ('hrreferencia', models.TimeField(blank=True, null=True)),
                ('cdespecie', models.CharField(blank=True, max_length=5, null=True)),
                ('cdseriesubserie', models.CharField(blank=True, max_length=5, null=True)),
                ('nrdocumento', models.CharField(blank=True, max_length=40, null=True)),
                ('stdocumentocancelado', models.CharField(blank=True, max_length=1, null=True)),
                ('tpdocumento', models.CharField(blank=True, max_length=1, null=True)),
                ('dsobservacao', models.CharField(blank=True, max_length=255, null=True)),
                ('tp12', models.CharField(blank=True, max_length=1, null=True)),
                ('vltotal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('aldesconto', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vldesconto', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlacrescimo', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alacrescimo', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alcomissao', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('idprazo', models.CharField(blank=True, max_length=40, null=True)),
                ('stexp', models.CharField(blank=True, max_length=1, null=True)),
                ('cdexterno', models.CharField(blank=True, max_length=20, null=True)),
                ('cdfiscal', models.CharField(blank=True, max_length=6, null=True)),
                ('stfiscal', models.CharField(blank=True, max_length=1, null=True)),
                ('tpciffob', models.CharField(blank=True, max_length=1, null=True)),
                ('usuario', models.CharField(blank=True, max_length=20, null=True)),
                ('vlsinal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('idtransportador', models.CharField(blank=True, max_length=40, null=True)),
                ('iddettransp', models.CharField(blank=True, max_length=40, null=True)),
                ('iddocabertura', models.CharField(blank=True, max_length=40, null=True)),
                ('calcicmsant', models.CharField(blank=True, max_length=1, null=True)),
                ('icmsfonte', models.CharField(blank=True, max_length=1, null=True)),
                ('vlrecolhido', models.CharField(blank=True, max_length=1, null=True)),
                ('bssubst', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlsubst', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bsicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('stsomadespbasesubst', models.CharField(blank=True, max_length=1, null=True)),
                ('stbasereduzidasubst', models.CharField(blank=True, max_length=1, null=True)),
                ('stsomadespbaseicms', models.CharField(blank=True, max_length=1, null=True)),
                ('stredbaseicms', models.CharField(blank=True, max_length=1, null=True)),
                ('stdeduzicms', models.CharField(blank=True, max_length=1, null=True)),
                ('stcalculasubst', models.CharField(blank=True, max_length=1, null=True)),
                ('stcalculaicms', models.CharField(blank=True, max_length=1, null=True)),
                ('vlseguro', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vloutros', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlfrete', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('idcontrolenf', models.CharField(blank=True, max_length=40, null=True)),
                ('vlipi', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bsipi', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('comissstabateicms', models.BooleanField(default=False)),
                ('stgeracomflux', models.BooleanField(default=False)),
                ('stipisomaicms', models.CharField(blank=True, max_length=1, null=True)),
                ('stipisomast', models.CharField(blank=True, max_length=1, null=True)),
                ('stdasomaipi', models.CharField(blank=True, max_length=1, null=True)),
                ('stsomasubstanota', models.CharField(blank=True, max_length=1, null=True)),
                ('stcalculaipi', models.CharField(blank=True, max_length=1, null=True)),
                ('stdesconto', models.CharField(blank=True, max_length=1, null=True)),
                ('stacrescimo', models.CharField(blank=True, max_length=1, null=True)),
                ('idoperacao', models.CharField(blank=True, max_length=40, null=True)),
                ('tpoperacao', models.CharField(blank=True, max_length=1, null=True)),
                ('usuariodecancelamento', models.CharField(blank=True, max_length=20, null=True)),
                ('stestorno', models.CharField(blank=True, max_length=1, null=True)),
                ('idpessoamaster', models.CharField(blank=True, max_length=40, null=True)),
                ('cdempvend', models.CharField(blank=True, max_length=3, null=True)),
                ('usuorcedicao', models.CharField(blank=True, max_length=20, null=True)),
                ('iddocestorno', models.CharField(blank=True, max_length=40, null=True)),
                ('tpdevolucao', models.CharField(blank=True, max_length=1, null=True)),
                ('vlttservicos', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlttiss', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlirretido', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('stcomplementoimposto', models.BooleanField(default=False)),
                ('idpedido', models.CharField(blank=True, max_length=40, null=True)),
                ('vlbonificacao', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cdorcamento', models.CharField(blank=True, max_length=15, null=True)),
                ('cd_atendimento', models.CharField(blank=True, max_length=15, null=True)),
                ('cdmodelo', models.CharField(blank=True, max_length=2, null=True)),
                ('bsicmsreduzida', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vldificms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('stvaloresalterados', models.BooleanField(default=False)),
                ('vlconhecimento', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('dsobservacaomemo', models.TextField(blank=True, null=True)),
                ('nrnsu', models.IntegerField(blank=True, null=True)),
                ('dtnsu', models.DateTimeField(blank=True, null=True)),
                ('vldiferimentoicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlpisret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlcofinsret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlinssret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlirret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlcsllret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlbasecsrf', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlbaseinssret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlbaseirrf', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tpdocumentofatura', models.CharField(blank=True, max_length=2, null=True)),
                ('emitentefatura', models.CharField(blank=True, max_length=1, null=True)),
                ('desccomplementarfatura', models.CharField(blank=True, max_length=50, null=True)),
                ('nrfatura', models.CharField(blank=True, max_length=40, null=True)),
                ('stemissaopropria', models.CharField(blank=True, max_length=1, null=True)),
                ('idsituacaodoc', models.CharField(blank=True, max_length=40, null=True)),
                ('stpessoaicmssimples', models.BooleanField(default=False)),
                ('vltotalnfe', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('stprodutoservico', models.BooleanField(default=False)),
                ('stajusteicms', models.BooleanField(default=False)),
                ('idnfe', models.CharField(blank=True, max_length=40, null=True)),
                ('stabateicmsdesonerado', models.BooleanField(default=False)),
                ('versao', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlterdataDocProds',
            fields=[
                ('iddocumentoitem', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('iddetalhe', models.CharField(blank=True, max_length=40, null=True)),
                ('idoperacao', models.CharField(blank=True, max_length=40, null=True)),
                ('iddocumento', models.CharField(blank=True, max_length=40, null=True)),
                ('stdocumentocancelado', models.CharField(blank=True, max_length=1, null=True)),
                ('idpessoa', models.CharField(blank=True, max_length=40, null=True)),
                ('tpoperacao', models.CharField(blank=True, max_length=1, null=True)),
                ('stacerto', models.CharField(blank=True, max_length=1, null=True)),
                ('statualizacusto', models.CharField(blank=True, max_length=1, null=True)),
                ('qtitem', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlitem', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlcusto', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alipi', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('idproduto', models.CharField(blank=True, max_length=40, null=True)),
                ('vlunitario', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlmovimento', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('stexp', models.CharField(blank=True, max_length=1, null=True)),
                ('cdexterno', models.CharField(blank=True, max_length=20, null=True)),
                ('alicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('tptributo', models.CharField(blank=True, max_length=1, null=True)),
                ('cdipi', models.CharField(blank=True, max_length=20, null=True)),
                ('sttrib', models.CharField(blank=True, max_length=3, null=True)),
                ('dssigla', models.CharField(blank=True, max_length=5, null=True)),
                ('vldescontorateado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vldesconto', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlacrescimorateado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlacrescimo', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cdfiscal', models.CharField(blank=True, max_length=6, null=True)),
                ('vlsubst', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bsicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bssubst', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('ufdestino', models.CharField(blank=True, max_length=2, null=True)),
                ('uforigem', models.CharField(blank=True, max_length=2, null=True)),
                ('alicmsinterna', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alreducaobase', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('allucrosubst', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlsegurorateado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlfreterateado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vloutrosrateado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bsipi', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlipi', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('stprodcomissionado', models.BooleanField(blank=True, null=True)),
                ('stvendaespecial', models.CharField(blank=True, max_length=1, null=True)),
                ('alacrescimo', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('aldesconto', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlunitariooriginal', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cdempvend', models.CharField(blank=True, max_length=3, null=True)),
                ('cdempresa', models.CharField(blank=True, max_length=3, null=True)),
                ('dtreferencia', models.DateTimeField(blank=True, null=True)),
                ('qtvolumes', models.IntegerField(blank=True, null=True)),
                ('tpdevolucao', models.CharField(blank=True, max_length=1, null=True)),
                ('bsiss', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('aliss', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alpis', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alcofins', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('qtdevolvida', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlconhecimentorateado', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlpisret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlcofinsret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlinssret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlirret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlcsllret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('naturezaoperacao', models.IntegerField(blank=True, null=True)),
                ('alpisret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alcofinsret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alinssret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alirret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alcsllret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlbasecsrf', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlbaseinssret', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlbaseirrf', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlmaterialservico', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('cdsittribcofins', models.CharField(blank=True, max_length=2, null=True)),
                ('cdsittribpis', models.CharField(blank=True, max_length=2, null=True)),
                ('stmovimentacaofisica', models.CharField(blank=True, max_length=1, null=True)),
                ('vlbasepis', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlbasecofins', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlpis', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlcofins', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('gtin', models.CharField(blank=True, max_length=14, null=True)),
                ('vlfcpicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bsfcpsubst', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlfcpsubst', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('bsfcpicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('alfcp', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vldificms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('vlreducaobaseicms', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlterdataProds',
            fields=[
                ('iddetalhe', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('idproduto', models.CharField(max_length=40)),
                ('idcaracteristica', models.CharField(blank=True, max_length=40, null=True)),
                ('dsdetalhe', models.CharField(blank=True, max_length=50, null=True)),
                ('iddetgradeh', models.CharField(blank=True, max_length=40, null=True)),
                ('iddetgradev', models.CharField(blank=True, max_length=40, null=True)),
                ('vlprecocusto', models.FloatField(blank=True, null=True)),
                ('vldesc1', models.FloatField(blank=True, null=True)),
                ('vldesc2', models.FloatField(blank=True, null=True)),
                ('tpdesc2', models.CharField(blank=True, max_length=1, null=True)),
                ('vlperipi', models.FloatField(blank=True, null=True)),
                ('vlperfrete', models.FloatField(blank=True, null=True)),
                ('vlpericms', models.FloatField(blank=True, null=True)),
                ('vloutros', models.FloatField(blank=True, null=True)),
                ('vlpermarkup', models.FloatField(blank=True, null=True)),
                ('vlprecovenda', models.FloatField(blank=True, null=True)),
                ('dsimagem', models.CharField(blank=True, max_length=20, null=True)),
                ('qtestoque', models.FloatField(blank=True, null=True)),
                ('qtestoque2', models.FloatField(blank=True, null=True)),
                ('qtexpminima', models.FloatField(blank=True, null=True)),
                ('qtminima', models.FloatField(blank=True, null=True)),
                ('qtmaxima', models.FloatField(blank=True, null=True)),
                ('qtcritica', models.FloatField(blank=True, null=True)),
                ('stpesado', models.CharField(blank=True, max_length=1, null=True)),
                ('steditadesc', models.CharField(blank=True, max_length=1, null=True)),
                ('stexp', models.CharField(blank=True, max_length=1, null=True)),
                ('cdexterno', models.CharField(blank=True, max_length=20, null=True)),
                ('tpclassifabcloja', models.CharField(blank=True, max_length=1, null=True)),
                ('tpclassifabcrede', models.CharField(blank=True, max_length=1, null=True)),
                ('percentvendaloja', models.FloatField(blank=True, null=True)),
                ('percentvendarede', models.FloatField(blank=True, null=True)),
                ('nrrankloja', models.IntegerField(blank=True, null=True)),
                ('nrrankrede', models.IntegerField(blank=True, null=True)),
                ('qtestoquecentral', models.IntegerField(blank=True, null=True)),
                ('obs', models.TextField(blank=True, null=True)),
                ('vlprecovendaant', models.FloatField(blank=True, null=True)),
                ('dtaltvlprecovenda', models.DateTimeField(blank=True, null=True)),
                ('statusalt', models.CharField(blank=True, max_length=3, null=True)),
                ('pesoliquido', models.FloatField(blank=True, null=True)),
                ('pesobruto', models.FloatField(blank=True, null=True)),
                ('cdprincipal', models.CharField(blank=True, max_length=20, null=True)),
                ('allucro', models.FloatField(blank=True, null=True)),
                ('stlojavirtual', models.CharField(blank=True, max_length=1, null=True)),
                ('qtembalagem', models.FloatField(blank=True, null=True)),
                ('allucrodesejada', models.FloatField(blank=True, null=True)),
                ('alcomissao', models.FloatField(blank=True, null=True)),
                ('stbalanca', models.BooleanField(blank=True, null=True)),
                ('stexpimg', models.CharField(blank=True, max_length=1, null=True)),
                ('stcomissionado', models.BooleanField(blank=True, null=True)),
                ('dtcadastro', models.DateTimeField(blank=True, null=True)),
                ('vlvendaabc', models.FloatField(blank=True, null=True)),
                ('qtvendaabc', models.FloatField(blank=True, null=True)),
                ('vllucroabc', models.FloatField(blank=True, null=True)),
                ('cdtratamentoespecial', models.CharField(blank=True, max_length=3, null=True)),
                ('vlvendaabcrede', models.FloatField(blank=True, null=True)),
                ('qtvendaabcrede', models.FloatField(blank=True, null=True)),
                ('vllucroabcrede', models.FloatField(blank=True, null=True)),
                ('dslocalizacao', models.CharField(blank=True, max_length=50, null=True)),
                ('idfamilia', models.CharField(blank=True, max_length=40, null=True)),
                ('stdesccomplementar', models.BooleanField(blank=True, null=True)),
                ('dsdesccomplementar', models.CharField(blank=True, max_length=200, null=True)),
                ('cdprodfiscal', models.CharField(blank=True, max_length=9, null=True)),
                ('idunidadecompra', models.CharField(blank=True, max_length=40, null=True)),
                ('stetiqgondola', models.BooleanField(blank=True, null=True)),
                ('ststretchimagem', models.BooleanField(blank=True, null=True)),
                ('sttrabalhaiss', models.BooleanField(blank=True, null=True)),
                ('aliss', models.FloatField(blank=True, null=True)),
                ('qtexpmaxima', models.FloatField(blank=True, null=True)),
                ('dtaltvlprecocusto', models.DateTimeField(blank=True, null=True)),
                ('idunidadetransf', models.CharField(blank=True, max_length=40, null=True)),
                ('dtaltallucrodesejada', models.DateTimeField(blank=True, null=True)),
                ('dtaltqtminima', models.DateTimeField(blank=True, null=True)),
                ('dtaltqtcritica', models.DateTimeField(blank=True, null=True)),
                ('dtaltnrrankloja', models.DateTimeField(blank=True, null=True)),
                ('dtaltpercentvendaloja', models.DateTimeField(blank=True, null=True)),
                ('dtalttpclassifabcloja', models.DateTimeField(blank=True, null=True)),
                ('dtaltqtexpminima', models.DateTimeField(blank=True, null=True)),
                ('dtaltqtexpmaxima', models.DateTimeField(blank=True, null=True)),
                ('dtaltidunidadetransf', models.DateTimeField(blank=True, null=True)),
                ('alipivenda', models.FloatField(blank=True, null=True)),
                ('alroyalties', models.FloatField(blank=True, null=True)),
                ('vlperpis', models.FloatField(blank=True, null=True)),
                ('vlpercofins', models.FloatField(blank=True, null=True)),
                ('stapurapiscofins', models.BooleanField(blank=True, null=True)),
                ('cdnatoperservico', models.CharField(blank=True, max_length=3, null=True)),
                ('tprecolhimentoiss', models.CharField(blank=True, max_length=1, null=True)),
                ('stinativo', models.BooleanField(blank=True, null=True)),
                ('naturezaoperacao', models.IntegerField(blank=True, null=True)),
                ('cdsittribpisentrada', models.CharField(blank=True, max_length=2, null=True)),
                ('cdsittribpis', models.CharField(blank=True, max_length=2, null=True)),
                ('cdsittribcofinsentrada', models.CharField(blank=True, max_length=2, null=True)),
                ('cdsittribcofins', models.CharField(blank=True, max_length=2, null=True)),
                ('cdsituacaooperacao', models.CharField(blank=True, max_length=3, null=True)),
                ('stmovimentaestoque', models.BooleanField(blank=True, null=True)),
                ('cdtribmunicipio', models.CharField(blank=True, max_length=20, null=True)),
                ('selofiscal', models.BooleanField(blank=True, null=True)),
                ('cod_seloipi', models.CharField(blank=True, max_length=6, null=True)),
                ('classeenquadraipi', models.CharField(blank=True, max_length=5, null=True)),
                ('cdsituacaooperacaost', models.CharField(blank=True, max_length=3, null=True)),
                ('origemmercadoria', models.CharField(blank=True, max_length=1, null=True)),
                ('cdcombustivelanp', models.CharField(blank=True, max_length=9, null=True)),
                ('alcargatributaria', models.FloatField(blank=True, null=True)),
                ('alpiscompra', models.FloatField(blank=True, null=True)),
                ('alcofinscompra', models.FloatField(blank=True, null=True)),
                ('dtaltvloutros', models.DateTimeField(blank=True, null=True)),
                ('fci', models.CharField(blank=True, max_length=36, null=True)),
                ('stconciliacaouniversosped', models.IntegerField(blank=True, null=True)),
                ('dtconciliacaouniversosped', models.DateTimeField(blank=True, null=True)),
                ('percgasnaturalglp', models.FloatField(blank=True, null=True)),
                ('alctfedimp', models.FloatField(blank=True, null=True)),
                ('alctest', models.FloatField(blank=True, null=True)),
                ('alctmun', models.FloatField(blank=True, null=True)),
                ('alctfednac', models.FloatField(blank=True, null=True)),
                ('pesoembalagem', models.FloatField(blank=True, null=True)),
                ('fatorconvetiqueta', models.FloatField(blank=True, null=True)),
                ('dsfatorconvetiqueta', models.CharField(blank=True, max_length=20, null=True)),
                ('stdetalheativo', models.BooleanField(blank=True, null=True)),
                ('cdnaturezareceita', models.CharField(blank=True, max_length=3, null=True)),
                ('stcardapio', models.BooleanField(blank=True, null=True)),
                ('percgasnaturalglpimp', models.FloatField(blank=True, null=True)),
                ('percgaspetroleo', models.FloatField(blank=True, null=True)),
                ('vlpartidaglp', models.FloatField(blank=True, null=True)),
                ('ftconvunidtributaria', models.FloatField(blank=True, null=True)),
                ('tpunidtributaria', models.CharField(blank=True, max_length=6, null=True)),
                ('alfcp', models.FloatField(blank=True, null=True)),
                ('qtvolumes', models.IntegerField(blank=True, null=True)),
                ('alsubsttrib', models.FloatField(blank=True, null=True)),
                ('percmva', models.FloatField(blank=True, null=True)),
                ('codigonbs', models.CharField(blank=True, max_length=9, null=True)),
            ],
        ),
    ]
