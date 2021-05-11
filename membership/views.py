from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Person, Household, StudentTeam, DuesPlan

def index(request):
    return render(request, 'membership/index.html', {})

ITEMS_PER_PAGE = 50
class PersonListView(LoginRequiredMixin, ListView):
    model = Person
    paginate_by = ITEMS_PER_PAGE

class PersonDetailView(LoginRequiredMixin, DetailView):
    model = Person

class HouseholdListView(LoginRequiredMixin, ListView):
    model = Household
    paginate_by = ITEMS_PER_PAGE

class HouseholdDetailView(LoginRequiredMixin, DetailView):
    model = Household

class StudentTeamListView(LoginRequiredMixin, ListView):
    model = StudentTeam
    paginate_by = ITEMS_PER_PAGE

class StudentTeamDetailView(LoginRequiredMixin, DetailView):
    model = StudentTeam

class DuesPlanListView(ListView):
    model = DuesPlan
    paginate_by = ITEMS_PER_PAGE

class DuesPlanDetailView(LoginRequiredMixin, DetailView):
    model = DuesPlan
