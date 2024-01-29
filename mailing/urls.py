from django.urls import path

from mailing.apps import MailingConfig
# from mailing.views import HomePageView, MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView


app_name = MailingConfig.name

urlpatterns = [
    # path('', HomePageView.as_view(), name='home'),
#     path('list/', MailingListView.as_view(), name='mailing_list'),
#     path('view/<int:pk>/', MailingDetailView.as_view(), name='mailing_view'),
#     path('create/', MailingCreateView.as_view(), name='mailing_create'),
#     path('edit/<int:pk>/', MailingUpdateView.as_view(), name='mailing_edit'),
#     path('delete/<int:pk>/', MailingDeleteView.as_view(), name='mailing_delete'),
 ]
