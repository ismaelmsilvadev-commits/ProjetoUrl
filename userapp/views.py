from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login

from .forms import RegisterForm


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = RegisterForm
    template_name = 'userapp/register.html'
    success_url = reverse_lazy('urlapp:index')
    success_message = "Conta criada! Bem-vindo(a)."

    def form_valid(self, form):
        response = super().form_valid(form)

        login(self.request, self.object)

        return response
