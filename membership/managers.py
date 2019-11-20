from django.db import models
# import django.utils.timezone

ACTIVE_STATUSES = ['active', 'past_due']

class MemberManager(models.Manager):
    def active(self):
        base_qs = self.get_queryset()
        regular_members = base_qs.filter(household__status__in=ACTIVE_STATUSES)
        student_members = base_qs.filter(student_team__status__in=ACTIVE_STATUSES)
        return regular_members.union(student_members)

class MembershipEntityManager(models.Manager):
    def active(self):
        self.get_queryset().filter(status__in=ACTIVE_STATUSES)
