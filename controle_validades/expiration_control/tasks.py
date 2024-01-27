from .utils.email import EmailHandler
from .models import Validade, Detalhe
from background_task import background
from datetime import datetime, timedelta


@background(schedule=10)
def notify_expiration(): 
    input('email')
    validades = Validade.objects.all().order_by('dtvalidade')
    today = datetime.today().date()
    limit_day = today + timedelta(days=7)
    vencidos = [val for val in validades if val.dtvalidade <= limit_day]
    recipients = ['thanatsuv3@gmail.com']
    subject = 'Produtos Vencidos e proximos de vencer'
    email = EmailHandler(recipients, vencidos, today, subject)
    email.send_email()
    

@background(schedule=10)
def add_promo_tag():
    print('begin')
    today = datetime.today().date()
    validades = Validade.objects.filter(dtvalidade__lte=today)[0:1]
    for validade in validades:
        iddetalhe = validade.produto.iddetalhe
        detalhe = Detalhe.objects.using('alterdata').get(iddetalhe=iddetalhe)
        detalhe.dsdetalhe += ' (PROMO)' 
        detalhe.save()
    print(detalhe)
    test = Detalhe.objects.using('alterdata').get(iddetalhe=iddetalhe)
    input(test.dsdetalhe)

add_promo_tag()


