from .utils.email import EmailHandler
from datetime import datetime, timedelta
from django.db import DataError, connections
from .models import Validade, Produto, Detalhe, Comissao, Product
from django.core.mail import EmailMultiAlternatives
import pandas as pd



def notify_expiration(): 
    validades = Validade.objects.all().order_by(
        'dtvalidade', 'produto__dsdetalhe'
    )
    today = datetime.today().date()
    limit_day = today + timedelta(days=120)
    vencidos = [val for val in validades if val.dtvalidade <= limit_day]
    recipients = ['thanatsuv3@gmail.com', 'viviannepimenta@grupoconstrufacil.com.br']
    subject = 'Produtos Vencidos e proximos de vencer'
    email = EmailHandler(recipients, vencidos, today, subject)
    email.send_email()
    
    # comissoes = Comissao.objects.filter(cdchamada='000054')
    # resultado = comissoes.values('cdchamada').annotate(soma_vltotal=Sum('vltotal'))
    # for item in resultado:
    #     print(f"cdchamada: {item['cdchamada']}, soma de vltotal: {item['soma_vltotal']}")


def add_promo_tag():
    errors_log = []
    today = datetime.today().date()
    limit_day = today + timedelta(days=90)
    validades = Validade.objects.filter(dtvalidade__lte=limit_day)
    
    for validade in validades:
        iddetalhe = validade.produto.iddetalhe
        detalhe = Detalhe.objects.using('alterdata').get(iddetalhe=iddetalhe)
        produto = Produto.objects.using('alterdata').get(idproduto=detalhe.idproduto)
        if '|PROMO' in detalhe.dsdetalhe:
            continue
        try:
            detalhe.dsdetalhe += ' |PROMO'
            produto.nmproduto = detalhe.dsdetalhe
            detalhe.save()
            produto.save()
        except DataError:
            errors_log.append(detalhe)
    body = 'Erros \n'
    for det in errors_log:
        body+= f'{det.dsdetalhe} tem a descrição muito grande, ajustar e colocar "|PROMO" manualmente\n'
    msg = EmailMultiAlternatives(
            f'Erro ao adicionar produtos nas promoções',
            body,
            'controledevalidade@grupoconstrufacil.com.br', 
            ['thanatsuv3@gmail.com'])
    msg.send()
    print('error mail sended')
    
def remove_promo_tag():
    validades = Validade.objects.filter(qtestoque__lte=0, stativo=True)
    for validade in validades:
        validade.stativo = False
        iddetalhe = validade.produto.iddetalhe
        detalhe = Detalhe.objects.using('alterdata').get(iddetalhe=iddetalhe)
        produto = Produto.objects.using('alterdata').get(idproduto=detalhe.idproduto)
        detalhe.dsdetalhe = detalhe.dsdetalhe.replace('|PROMO', '')
        produto.nmproduto = produto.nmproduto.replace('|PROMO', '')
        validade.save()
        produto.save()
        detalhe.save()
        
def update_sales():
    connection = connections['alterdata']
    with connection.cursor() as cursor: 
        sql_query = """
            SELECT item.iddetalhe, item.iddocumentoitem,
            item.qtitem, item.vlunitario, item.vldesconto,
            det.vlpermarkup, det.cdprincipal, doc.cdorcamento,
            pes.nmpessoa, pes.cdchamada, doc.iddocumento, det.dsdetalhe,
            doc.dsobservacao
            FROM docitem as item
            JOIN documen as doc on doc.iddocumento = item.iddocumento
            JOIN detalhe as det on det.iddetalhe = item.iddetalhe
            JOIN wshop.comitem AS com ON com.iddocitem = item.iddocumentoitem
            JOIN wshop.pessoas AS pes ON com.idpessoa = pes.idpessoa
            WHERE doc.dtemissao BETWEEN '15/02/2023' AND '15/07/2023'
            AND doc.tpoperacao = 'V'
        """
        cursor.execute(sql_query)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        results_list = [
            {column: value for column, value in zip(columns, row)}
                for row in rows
        ]
    keyword = '|PROMO'
    margem = False
    promo_sales = []
    for row in results_list:
        if keyword in row['dsdetalhe'] and keyword in row['dsobservacao']:
            comissao = {}
            if not row['vldesconto']:
                margem = 0.30
            else:
                desconto_unitario = row['vldesconto'] / row['qtitem']
                desconto_percentual = desconto_unitario / (row['vlunitario'] * 100)
                
                if desconto_percentual > 10:
                    margem = 0.075
                else: 
                    margem = 0.15
           
            if not margem:
                raise ValueError('Commisao sempre deveria ter margem')
            else:
                
                validades = Validade.objects.filter(
                    stativo=True, produto__cdprincipal=row['cdprincipal']
                )
                if not validades.exists():
                    raise ValueError('esse produto não esta na lista de validades')
                    
                comissao['iddocumentoitem'] = row['iddocumentoitem']
                comissao['iddocumento'] = row['iddocumento']
                comissao['cdorcamento'] = row['cdorcamento']
                comissao['produto'] = Product.objects.get(cdprincipal=row['cdprincipal']) 
                comissao['dsvendedor'] = row['nmpessoa']
                comissao['cdchamada'] = row['cdchamada']
                comissao['vltotal'] = row['vlunitario'] * (row['vlpermarkup'] / 100) * margem
                promo_sales.append(comissao)
                validade_filtradas = []
                soma_validades_qtestoque = 0
                for validade in validades:
                    soma_validades_qtestoque += validade.qtestoque
                    
                if soma_validades_qtestoque < row['qtitem']:
                    raise ValueError("row['qtitem'] deveria ser meno do que a soma de validades")
                
                for validade in validade_filtradas:
                    
                    if (row['qtitem'] - validade.qtestoque) > 0:
                        row['qtitem'] -= validade.qtestoque
                        validade.qtestoque =- validade.qtestoque
                    else: 
                        validade.qtestoque -= row['qtitem']
                    validade.save()
    
    final_result = [promo for promo in promo_sales if not Comissao.objects.filter(
        iddocumento=promo['iddocumento'], iddocumentoitem=promo['iddocumentoitem'],
        produto=promo['produto']
        ).exists()]
    
    if final_result:
        Comissao.objects.bulk_create([Comissao(**promo) for promo in promo_sales])
    


def salvar_vencidos():
    with open('ven.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    try:
        for line in lines:
       
            produto = Product.objects.get(cdprincipal=line.split(':')[0].strip())
            instance = Validade(
                produto=produto,
                dtvalidade=datetime.strptime(line.split(':')[1].strip(), '%d/%m/%y'),
                qtestoque=int(line.split(':')[2].strip()),
            )
            instance.save()
    except Product.DoesNotExist:
        alterdata_produto = Detalhe.objects.using('alterdata').get(cdprincipal=line.split(':')[0].strip())
        produto = Product(
                iddetalhe=alterdata_produto.iddetalhe, cdprincipal=alterdata_produto.cdprincipal,
                dsdetalhe=alterdata_produto.dsdetalhe
            )
        produto.save()
        instance = Validade(
                produto=produto,
                dtvalidade=datetime.strptime(line.split(':')[1].strip(), '%d/%m/%y'),
                qtestoque=int(line.split(':')[2].strip()),
            )
        
def gerar_relatorio():
    validades = Validade.objects.all().order_by(
        'dtvalidade', 'produto__dsdetalhe'
    )
    today = datetime.today().date()
    vencidos = [val for val in validades if val.dtvalidade <= today]
    
    # Cria uma lista de dicionários, onde cada dicionário contém os dados que você quer
    dados = [{
        'dtvalidade': val.dtvalidade,
        'cdprincipal': val.produto.cdprincipal,
        'dsdetalhe': val.produto.dsdetalhe
    } for val in vencidos]

    for dado in dados:
        
        det = Detalhe.objects.using('alterdata').get(cdprincipal=dado['cdprincipal'])
        prod = Produto.objects.using('alterdata').get(idproduto=det.idproduto)
        
        preco_venda = det.vlprecovenda

        # Margem de lucro em porcentagem
        margem_lucro_percentual = det.allucro

        # Convertendo a porcentagem de lucro para um fator multiplicador
        fator_multiplicador = 1 + (margem_lucro_percentual / 100)

        # Calculando o custo
        custo = preco_venda / fator_multiplicador

        dado['custo'] =  custo
        dado['tributação'] = prod.tributacao
        
    df = pd.DataFrame(dados)

    df.to_excel('relatorio.xlsx')
