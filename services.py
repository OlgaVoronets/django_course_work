from django.conf import settings
from django.core.mail import send_mail

NULLABLE = {'null': True, 'blank': True}

"""Статусы рассылки"""
STATUS_CHOICES = [
    ('created', 'Создана'),
    ('started', 'Запущена'),
    ('completed', 'Завершена'),
]
"""Периодичность рассылки"""
PERIOD_CHOICES = [
    ('once', '1 раз'),
    ('daily', 'Ежедневно'),
    ('weekly', 'Еженедельно'),
    ('monthly', 'Ежемесячно'),
]
"""Статус рассылки для лога"""
LOG_CHOICES = [
    (True, 'Успешно'),
    (False, 'Ошибка')
]


class StileFormMixin:
    """Класс-миксин для стилизации форм """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


def send_mailing(new_user):
    """Функция отправки сообщения с кодом подтверждения регистрации"""
    send_mail(
            subject='Подтверждение регистрации',
            message=f'Код подтверждения  {new_user.verify_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )











































































































# def send_mailing(mailing):
#     now = timezone.localtime(timezone.now())
#     if mailing.start_point <= now <= mailing.stop_point:
#         for message in mailing.send_to.all():
#             for client in mailing.clients.all():
#                 try:
#                     result = send_mail(
#                         subject=message.title,
#                         message=message.text,
#                         from_email=settings.EMAIL_HOST_USER,
#                         recipient_list=[client.email],
#                         fail_silently=False
#                     )
#                     log = Log.objects.create(
#                         time=mailing.start_time,
#                         status=result,
#                         server_response='OK',
#                         mailing_list=mailing,
#                         client=client
#                     )
#                     log.save()
#                     return log
#                 except SMTPException as error:
#                     log = Log.objects.create(
#                         time=mailing.start_time,
#                         status=False,
#                         server_response=error,
#                         mailing_list=mailing,
#                         client=client
#                     )
#                     log.save()
#                 return log
#     else:
#         mailing.status = MailingSettings.COMPLETED
#         mailing.save()


# def daily_tasks():
#     mailings = MailingSettings.objects.filter(periodicity="Раз в день", status="Запущена")
#     if mailings.exists():
#         for mailing in mailings:
#             send_mailling(mailing)
#
#
# def weekly_tasks():
#     mailings = MailingSettings.objects.filter(periodicity="Раз в неделю", status="Запущена")
#     if mailings.exists():
#         for mailing in mailings:
#             send_mailling(mailing)
#
#
# def monthly_tasks():
#     mailings = MailingSettings.objects.filter(periodicity="Раз в месяц", status="Запущена")
#     if mailings.exists():
#         for mailing in mailings:
#             send_mailling(mailing)