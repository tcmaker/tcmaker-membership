from django.urls import path
from . import views

app_name = 'webhooks'
urlpatterns = [
    path('', views.receive_webhook, name="receive_webhook"),
]
