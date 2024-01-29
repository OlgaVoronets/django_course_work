import datetime
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail

from mailing.models import Mailing, Log


class StileFormMixin:
    """Класс-миксин для стилизации форм """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# def send_mailing(mailing):
#     now = datetime.datetime.now()
#     if mailing.start_point <= now <= mailing.stop_point:
#         for message in mailing.messages.all():
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
#                         time=mailing.start_point,
#                         status=result,
#                         server_response='OK',
#                         mailing_list=mailing,
#                         client=client
#                     )
#                     log.save()
#                     return log
#                 except SMTPException as error:
#                     log = Log.objects.create(
#                         time=mailing.start_point,
#                         status=False,
#                         server_response=error,
#                         mailing_list=mailing,
#                         client=client
#                     )
#                     log.save()
#                 return log
#     else:
#         mailing.status = Mailing.completed
#         mailing.save()
#

def my_job():
    now = datetime.datetime.now()
    mailings = Mailing.objects.filter(status="started")
    for mailing in mailings:
        if mailing.start_point <= now <= mailing.stop_point:
            for message in mailing.messages.all():
                for client in mailing.clients.all():
                        send_mail(
                            subject=message.title,
                            message=message.text,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[client.email],
                            fail_silently=False
                        )

# def daily_tasks():
#     mailings = Mailing.objects.filter(period="daily", status="started")
#     if mailings.exists():
#         for mailing in mailings:
#             send_mailing(mailing)
#             print('ежедневная')
#
#
# def weekly_tasks():
#     mailings = Mailing.objects.filter(period="weekly", status="started")
#     if mailings.exists():
#         for mailing in mailings:
#             send_mailing(mailing)
#
#
# def monthly_tasks():
#     mailings = Mailing.objects.filter(period="monthly", status="started")
#     if mailings.exists():
#         for mailing in mailings:
#             send_mailing(mailing)
#
#
#
#