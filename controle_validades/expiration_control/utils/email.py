from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailHandler:

    def __init__(self, recipient_list, vencidos, today, subject) -> None:
        self.recipient_list = recipient_list
        self.vencidos = vencidos
        self.from_email = 'controledevalidade@grupoconstrufacil.com.br'
        self.today = today
        self.subject = subject
        self.html_content, self.text_content = self.get_html_template()
        self.msg = self.build_email()

    def get_html_template(self) -> str:
        html_content = render_to_string(
            'email/expired.html', {'vencidos': self.vencidos, 'today': self.today}
        )
        text_content = strip_tags(html_content)
        return html_content, text_content

    def build_email(self) -> EmailMultiAlternatives:
        msg = EmailMultiAlternatives(
            self.subject, self.text_content, self.from_email, self.recipient_list)
        msg.attach_alternative(self.html_content, "text/html")
        return msg
    
    def send_email(self):
        try:
            self.msg.send()
            print('E-mail HTML enviado com sucesso!')
        except Exception as e:
            print(e)
