from .utils.email import EmailHandler
from .models import Validade, Detalhe, Produto
from background_task import background
from datetime import datetime, timedelta


# @background(schedule=1000)
# def notify_expiration(): 
#     print('email')
#     validades = Validade.objects.all().order_by('dtvalidade')
#     today = datetime.today().date()
#     limit_day = today + timedelta(days=7)
#     vencidos = [val for val in validades if val.dtvalidade <= limit_day]
#     recipients = ['thanatsuv3@gmail.com']
#     subject = 'Produtos Vencidos e proximos de vencer'
#     email = EmailHandler(recipients, vencidos, today, subject)
#     email.send_email()
    

@background(schedule=1000)
def add_promo_tag():
    print('begin')
    today = datetime.today().date()
    validades = Validade.objects.filter(dtvalidade__lte=today)
    for validade in validades:
        if '(PROMO)' in validade.produto.dsdetalhe:
            print('have')
            continue
        iddetalhe = validade.produto.iddetalhe
        detalhe = Detalhe.objects.using('alterdata').get(iddetalhe=iddetalhe)
        produto = Produto.objects.using('alterdata').get(idproduto=detalhe.idproduto)
        detalhe.dsdetalhe += ' (PROMO)'
        produto.nmproduto = detalhe.dsdetalhe
        detalhe.save()
        produto.save()
    print('done')
add_promo_tag()


