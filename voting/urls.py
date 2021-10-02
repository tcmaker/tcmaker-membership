from django.urls import path
from . import views

app_name = 'voting'
urlpatterns = [
    path('', views.voting_list_2021, name="index"),
    path('csv/', views.voting_list_2021_csv, name="csv")
]
