from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from membership.models import Person

import uuid

class BaseEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField('Notes', null=True, blank=True, help_text='Only staff will be able to view these notes')

    class Meta:
        abstract = True

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
