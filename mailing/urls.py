from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import HomePageView, MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, \
    MailingDeleteView, ClientListView, ClientCreateView, ClientUpdateView, LogListView

app_name = MailingConfig.name

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('list/', MailingListView.as_view(), name='mailing_list'),
    path('view/<int:pk>/', MailingDetailView.as_view(), name='mailing_view'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),
    path('delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
    path('client_list/', ClientListView.as_view(), name='client_list'),
    path('client_create/', ClientCreateView.as_view(), name='client_create'),
    path('client_edit/<int:pk>/', ClientUpdateView.as_view(), name='client_edit'),
    path('log_list/', LogListView.as_view(), name='log_list'),

]
