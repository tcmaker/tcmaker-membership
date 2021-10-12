from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now as tz_now


from membership.models import Person

import uuid

class BaseEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField('Notes', null=True, blank=True, help_text='Only staff will be able to view these notes')

    class Meta:
        abstract = True

class AccessOverride(BaseEntity):
    description = models.CharField(max_length=100, blank=False, null=False)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    start_at = models.DateTimeField(blank=False, null=False)
    end_at = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.description

class Keyfob(BaseEntity):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    code = models.CharField(max_length=30, null=False, blank=False)
    access_level = models.PositiveSmallIntegerField(null=False, blank=False)
    is_active = models.BooleanField("Is this the member's active keyfob?", null=False, blank=False, default=True)

    def save(self, *args, **kwargs):
        old_keyfobs = Keyfob.objects.filter(person_id=self.person_id)
        old_keyfobs = old_keyfobs.exclude(id=self.id)
        old_keyfobs.update(is_active=False)
        return super().save(*args, **kwargs)

    def __str__(self):
        return "%s, %s: %s" % (
            self.person.family_name,
            self.person.given_name,
            self.code
        )


    def compute_is_membership_valid(self):
        # Hack to appease impatient shop managers
        now = tz_now()
        if self.person.accessoverride_set.filter(start_at__lte=now, end_at__gte=now).count() > 0:
            return True

        # business as usual
        if self.person.household:
            return self.person.household.status == 'active'
        if self.person.student_team:
            return self.person.student_team.status == 'active'

        # no dice
        return False

    # Hack to appease impatient shop managers
    def compute_membership_valid_through(self):
        now = tz_now()
        overrides = self.person.accessoverride_set.filter(start_at__lte=now, end_at__gte=now)
        if overrides:
            override = overrides.latest('end_at')
            return override.end_at

        # business as usual
        return self._old_compute_membership_valid_through()

        # Hack to appease impatient shop managers
        try:
            override = self.person.accessoverride_set.latest('end_at')
            return override.end_at
        except:
            return None

    def _old_compute_membership_valid_through(self):
        # business as usual
        if self.person.household:
            return self.person.household.valid_through
        if self.person.student_team:
            return self.person.student_team.valid_through

        # no dice
        return None


    def membership_valid_through(self):
        pass
