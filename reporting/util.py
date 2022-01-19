from django.utils import timezone
from .models import DailySummary

from membership.models import Household, StudentTeam

def create_todays_summary():
    cutoff = timezone.now()

    summary = DailySummary()
    summary.date = cutoff.date()

    for household in Household.objects.filter(valid_through__gte=cutoff):
        count = household.person_set.count()
        summary.active_members_total += count
        if count > 1:
            summary.active_households_multiperson += 1
        else:
            summary.active_households_singleperson += 1

    for team in StudentTeam.objects.filter(valid_through__gte=cutoff):
        summary.active_student_teams += 1
        summary.active_student_team_members += team.person_set.count()

    summary.save()
    return summary
