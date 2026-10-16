from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import RegisterForm


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'userapp/register.html'
    success_url = reverse_lazy('urlapp:index')
    success_message = "Conta criada! Bem-vindo(a)."
