from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CadastroUsuarioForm
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = CadastroUsuarioForm

    template_name = 'userapp/register.html'

    success_url = reverse_lazy('urlapp:index')

    success_message = "Your account has been created! Now you can login."
