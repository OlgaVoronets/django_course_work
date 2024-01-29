from django.forms import inlineformset_factory
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from mailing.forms import ClientForm, MailingForm, MessageForm
from mailing.models import Mailing, Client, Message


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
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home')

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        message_formset = inlineformset_factory(Mailing, Message, form=MessageForm, extra=1)

        if self.request.method == 'POST':
            context_data['formset'] = message_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = message_formset(instance=self.object)

        return context_data


class MailingUpdateView(UpdateView):
    """Редактирование рассылки"""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailing:home')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        message_formset = inlineformset_factory(Mailing, Message, form=MessageForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = message_formset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = message_formset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


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
    success_url = reverse_lazy('mailing:client_list')


class ClientUpdateView(UpdateView):
    """Редактирование карточки клиента"""
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('mailing:client_list')


