from django.urls import path
from . import views

app_name = "urlapp"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug:code>', views.RedirectUrlView.as_view(), name='redirect'),
]
