from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class LoginUsuarioForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CadastroUsuarioForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Usuario

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
