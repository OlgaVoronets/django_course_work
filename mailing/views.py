from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import ClientForm
from mailing.models import Mailing, Client


class HomePageView(TemplateView):
    """Отображение домашней страницы"""
    template_name = 'mailing/base.html'


class MailingListView(ListView):
    """Просмотр списка рассылок"""
    model = Mailing


class MailingDetailView(DetailView):
    """Просмотр рассылки по id"""
    model = Mailing


class MailingCreateView(CreateView):
    """Создание рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:home')


class MailingUpdateView(UpdateView):
    """Редактирование рассылки"""
    model = Mailing
    fields = '__all__'
    success_url = reverse_lazy('mailing:home')


class MailingDeleteView(DeleteView):
    """Удаление рассылки"""
    model = Mailing
    success_url = reverse_lazy('mailing:home')


class ClientListView(ListView):
    """Просмотр списка клиентов"""
    model = Client


class ClientCreateView(CreateView):
    """Создание карточки клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')


class ClientUpdateView(UpdateView):
    """Редактирование карточки клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')


