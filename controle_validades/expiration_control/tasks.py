from django.forms import model_to_dict
from .utils.email import EmailHandler
from background_task import background
from datetime import date, datetime, timedelta
from django.db import DataError, connections
from django.utils import timezone
from .models import Validade, Produto, Detalhe, Comissao, Product
from django.db.models import Sum
from django.core.mail import EmailMultiAlternatives

@background(schedule=1)
def notify_expiration(): 
    print('email')
    validades = Validade.objects.all().order_by('dtvalidade')
    today = datetime.today().date()
    limit_day = today + timedelta(days=120)
    vencidos = [val for val in validades if val.dtvalidade <= limit_day]
    recipients = ['thanatsuv3@gmail.com']
    subject = 'Produtos Vencidos e proximos de vencer'
    email = EmailHandler(recipients, vencidos, today, subject)
    email.send_email()
    
    # comissoes = Comissao.objects.filter(cdchamada='000054')
    # resultado = comissoes.values('cdchamada').annotate(soma_vltotal=Sum('vltotal'))
    # for item in resultado:
    #     print(f"cdchamada: {item['cdchamada']}, soma de vltotal: {item['soma_vltotal']}")


@background(schedule=1)
def add_promo_tag():
    errors = []
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
            errors.append(detalhe)
    body = 'Erros \n'
    for det in errors:
        body+= f'{det.dsdetalhe} tem a descrição muito grande, ajustar e colocar "|PROMO" manualmente\n'
    msg = EmailMultiAlternatives(
            f'Erro ao adicionar produtos nas promoções',
            body,
            'controledevalidade@grupoconstrufacil.com.br', 
            ['thanatsuv3@gmail.com'])
    msg.send()
    print('error mail sended')
    

@background(schedule=1)
def update_db():
    
    connection = connections['alterdata']
    with connection.cursor() as cursor: 
        sql_query = """
            SELECT item.iddetalhe, item.iddocumentoitem,
            item.qtitem, item.vlunitario, item.vldesconto,
            det.vlpermarkup, det.cdprincipal, doc.cdorcamento,
            pes.nmpessoa, pes.cdchamada, doc.iddocumento, det.dsdetalhe
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
        if keyword in row['dsdetalhe']:
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
                comissao['iddocumentoitem'] = row['iddocumentoitem']
                comissao['iddocumento'] = row['iddocumento']
                comissao['cdorcamento'] = row['cdorcamento']
                comissao['produto'] = Product.objects.get(cdprincipal=row['cdprincipal']) 
                comissao['dsvendedor'] = row['nmpessoa']
                comissao['cdchamada'] = row['cdchamada']
                comissao['vltotal'] = row['vlunitario'] * (row['vlpermarkup'] / 100) * margem
                promo_sales.append(comissao)
    final_result = [promo for promo in promo_sales if not Comissao.objects.filter(
        iddocumento=promo['iddocumento'], iddocumentoitem=promo['iddocumentoitem'],
        produto=promo['produto']
        ).exists()]
    if final_result:
        Comissao.objects.bulk_create([Comissao(**promo) for promo in promo_sales])
    
update_db()
notify_expiration()
add_promo_tag()