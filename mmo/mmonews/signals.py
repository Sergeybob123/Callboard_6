from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template import context
from django.template.loader import render_to_string

@receiver(post_save, sender=Advert)
def create_advert(sender, instance, created, **kwargs):
    if created:
        print(f'{instance.title} {instance.created.strftime("%Y-%M-%d")}')

@receiver(post_save, sender=Response)
def send_message_appointment(sender, instance, created, **kwargs):
    if created and instance.user.email:
        print(f'''Пользователь {instance.user.email}, откликнулся на ваш пост - '{instance.advert.content}' ''')

        html_content = render_to_string(template_name='email_message.html', context:{'instance': instance, })

        msg = EmailMultiAlternatives(
            subject=f'Отклик на пост - {instance.text}'
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.advert.user.email],
        )
        msg.attach_alternative(html_content, mimetype="text/html")
        msg.send()
