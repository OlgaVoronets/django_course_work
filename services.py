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


def my_job():
    now = datetime.datetime.now()
    mailings = Mailing.objects.filter(status="started")
    for mailing in mailings:
        if mailing.start_point <= now <= mailing.stop_point:
            for message in mailing.messages.all():
                for client in mailing.clients.all():
                    try:
                        response = send_mail(
                            subject=message.title,
                            message=message.text,
                            from_email=settings.EMAIL_HOST_USER,
                            recipient_list=[client.email],
                            fail_silently=False
                        )
                        mailing_log = Log.object.create(
                            attempt_time=mailing.start_point,
                            attempt_status=True,
                            server_response=response,
                            mailing=mailing,
                            client=client)
                        mailing_log.save()
                        if mailing.period == 'daily':
                            mailing.start_point += datetime.timedelta(days=1)
                        elif mailing.period == 'weekly':
                            mailing.start_point += datetime.timedelta(days=7)
                        elif mailing.period == 'monthly':
                            mailing.start_point += datetime.timedelta(days=30)
                        print(mailing_log)
                    except Exception as error:
                        mailing_log = Log.object.create(
                            attempt_time=mailing.start_point,
                            attempt_status=True,
                            server_response=error,
                            mailing=mailing,
                            client=client)
                        mailing_log.save()
                        print(mailing_log)
