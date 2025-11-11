from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.views.generic import ListView
from .models import EmailInfo

# Create your views here.


class EmailCreate(CreateView):
    model = EmailInfo
    fields = ['firstName', 'lastName', 'emailAdress']
    template_name = "emailCreate.html"
    success_url = "/home/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EmailCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('Email_detail', kwargs={'pk': self.object.pk})