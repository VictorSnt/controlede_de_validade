from .utils.email import EmailHandler
from .models import Validade, Detalhe, Produto
from background_task import background
from datetime import datetime, timedelta


@background(schedule=10)
def notify_expiration(): 
    print('email')
    validades = Validade.objects.all().order_by('dtvalidade')
    today = datetime.today().date()
    limit_day = today + timedelta(days=90)
    vencidos = [val for val in validades if val.dtvalidade <= limit_day]
    recipients = ['thanatsuv3@gmail.com']
    subject = 'Produtos Vencidos e proximos de vencer'
    email = EmailHandler(recipients, vencidos, today, subject)
    email.send_email()
notify_expiration()

@background(schedule=10)
def add_promo_tag():
    print('begin')
    today = datetime.today().date()
    limit_day = today + timedelta(days=45)
    validades = Validade.objects.filter(dtvalidade__lte=limit_day)
    for validade in validades:
        iddetalhe = validade.produto.iddetalhe
        detalhe = Detalhe.objects.using('alterdata').get(iddetalhe=iddetalhe)
        produto = Produto.objects.using('alterdata').get(idproduto=detalhe.idproduto)
        if '|PROMO' in detalhe.dsdetalhe:
            continue
        detalhe.dsdetalhe += ' |PROMO'
        produto.nmproduto = detalhe.dsdetalhe
        detalhe.save()
        produto.save()
    print('done')
add_promo_tag()

@background(schedule=10)
def add_comissao():
    pass
