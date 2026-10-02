from django.urls import path
from . import views

app_name = "urlapp"
urlpatterns = [
    path('<slug:code>', views.RedirectUrlView.as_view(), name='redirect'),
]
