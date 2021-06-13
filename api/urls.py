from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'persons', views.PersonViewSet)
router.register(r'households', views.HouseholdViewSet)
router.register(r'student_teams', views.StudentTeamViewSet)
router.register(r'dues_plans', views.DuesPlanViewSet)
router.register(r'keyfobs', views.KeyfobViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
