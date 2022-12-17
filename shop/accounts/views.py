from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class UserRegisterView(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name='registration/register.html'