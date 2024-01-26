from background_task import background
from .models import Validade
from datetime import datetime, timedelta
from django.core.mail import send_mail


@background(schedule=10)
def notify_expiration(): 
    
    validades = Validade.objects.all().order_by('-dtvalidade')
    limit_day = datetime.today().date() + timedelta(days=7)
    vencidos = [val for val in validades if val.dtvalidade <= limit_day]
    subject = 'Assunto do E-mail'
    message = 'Corpo do E-mail [0]}'
    from_email = 'conferentedenotas@grupoconstrufacil.com.br'
    recipient_list = ['thanatsuv3@gmail.com']
    print('done1')
    send_mail(subject, message, from_email, recipient_list)    
    print('done')
    
notify_expiration()