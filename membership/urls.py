from django.urls import path
from . import views

app_name = 'membership'
urlpatterns = [
    path('', views.index, name="index"),

    path('people/', views.PersonListView.as_view(), name="person_list"),
    # path('people/create/', views.PersonCreateView.as_view(), name="person_create"),
    path('people/<pk>/', views.PersonDetailView.as_view(), name="person_detail"),
    # path('people/<pk>/edit', views.PersonEditView.as_view(), name="person_edit"),

    path('households/', views.HouseholdListView.as_view(), name="household_list"),
    # path('households/create/', views.HouseholdCreateView.as_view(), name="household_create"),
    path('households/<pk>/', views.HouseholdDetailView.as_view(), name="household_detail"),
    # path('households/<pk>/edit', views.HouseholdEditView.as_view(), name="person_edit"),

    path('student-teams/', views.StudentTeamListView.as_view(), name="student_team_list"),
    # path('student-teams/create/', views.StudentTeamCreateView.as_view(), name="student_team_create"),
    path('student-teams/<pk>/', views.StudentTeamDetailView.as_view(), name="student_team_detail"),

    # We don't allow editing these through the normal interface. You have to
    # break the glass and use the admin panel.
    path('discounts/', views.DiscountListView.as_view(), name="discount_list"),
    path('discounts/<pk>/', views.DiscountDetailView.as_view(), name="discount_detail"),

    path('dues-plans/', views.DuesPlanListView.as_view(), name="dues_plan_list"),
    path('dues-plans/<pk>/', views.DuesPlanDetailView.as_view(), name="dues_plan_detail"),
]
