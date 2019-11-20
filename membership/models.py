from django.db import models

from django.db import models, DataError
from django.core.exceptions import ValidationError
from django.urls import reverse as url_reverse
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.us.models import USStateField, USZipCodeField
from model_utils import FieldTracker
import uuid, datetime
from django.utils.timezone import now as tz_now
from . import managers

class BaseEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    notes = models.TextField('Notes', null=True, blank=True, help_text='Only staff will be able to view these notes')

    class Meta:
        abstract = True

class Person(BaseEntity):
    # Basic Information
    given_name = models.CharField('Given Name', max_length=100)
    family_name = models.CharField('Family Name', max_length=100)
    email = models.EmailField('Email Address')
    member_since = models.DateField('Date Joined')

    household = models.ForeignKey('Household', on_delete=models.SET_NULL, blank=True, null=True)
    student_team = models.ForeignKey('StudentTeam', on_delete=models.SET_NULL, blank=True, null=True)

    # Address
    address_street1 = models.CharField('Street Address', max_length=100)
    address_street2 = models.CharField('Street Address 2', max_length=100, blank=True, null=True)
    address_city = models.CharField('City', max_length=100)
    address_state = USStateField('State')
    address_zip = USZipCodeField('Zip Code')

    # Phone Info
    phone_number = PhoneNumberField()
    phone_can_receive_sms = models.BooleanField(null=False, default=False)

    # Emergency Contact Information
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = PhoneNumberField()

    # Building Access
    keyfob_code = models.CharField('Keyfob Code', max_length=100)

    # Managers
    objects = managers.MemberManager()

    # This tells us which fields have been modified so custom save methods
    # and signal handlers can do less work.
    tracker = FieldTracker()

    def __str__(self):
        return ", ".join([self.family_name, self.given_name])

    def address_lines(self):
        ret = [self.address_street1]

        if self.address_street2:
            ret.append(self.address_street2)

        ret.append("%s %s, %s" % (
            self.address_city,
            self.address_state,
            self.address_zip))

        return ret

    def membership_status(self):
        if self.household:
            return self.household.status
        if self.student_team:
            return self.student_team.status
        return 'none'

    #### custom validation of member fields ####
    def __household_has_vacancies(self):
        if self.household == None:
            return True

        if self.household.has_vacancy_for(self):
            return True

        return False

    def clean(self):
        if not self.__household_has_vacancies():
            raise ValidationError({
                'household': 'The household is already full.'
            })

        if self.household and self.student_team:
            raise ValidationError({
                'household': 'One cannot join both a household and a student team',
                'student_team': 'One cannot join both a household and a student team',
            })

        super().clean()

    def save(self, *args, **kwargs):
        if not self.tracker.has_changed('household_id'):
            return super().save(*args, **kwargs)

        if not self.__household_has_vacancies():
            raise DataError('Household is already full')

        if self.household_id and self.student_team_id:
            raise DataError('One cannot join both a household and a student team')

        # we're in the clear
        super().save(*args, **kwargs)

class Discount(BaseEntity):
    stripe_coupon_identifier = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    description = models.TextField(help_text="Who qualifies for this discount, and what are its terms?")
    allow_family_memberships = models.BooleanField('Allow family memberships?', default=False)

    # This tells us which fields have been modified so custom save methods
    # and signal handlers can do less work.
    tracker = FieldTracker()

    def __str__(self):
        return self.name

class DuesPlan(BaseEntity):
    stripe_plan_identifier = models.CharField(max_length=100, help_text="Don't change this.")
    name = models.CharField(max_length=30, help_text='This text will appear in member-facing forms, so pick clear and descriptive.')
    requires_setup_fee = models.BooleanField(default=True)
    # requires_staff_approval = models.BooleanField(default=True, help_text='Student discounts, staff discounts, etc.')
    sort_priority = models.IntegerField(default=100)

    # This tells us which fields have been modified so custom save methods
    # and signal handlers can do less work.
    tracker = FieldTracker()

    def __str__(self):
        return self.name

MEMBERSHIP_STATUSES = [
    ('incomplete', 'Incomplete'),
    ('active', 'Active'),
    ('incomplete_expired', 'Incomplete (Expired)'),
    ('past_due', 'Past Due'),
    ('canceled', 'Canceled'),
    ('unpaid', 'Unpaid'),
]

class MembershipEntity(BaseEntity):
    name = models.CharField('Name', max_length=100, help_text='e.g. Team SkyNet')
    valid_through = models.DateField()
    contact = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='administered_%(class)s')
    valid_through = models.DateTimeField()
    status = models.CharField('Status', choices=MEMBERSHIP_STATUSES, default='incomplete', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

    # Managers
    objects = managers.MembershipEntityManager()

class StudentTeam(MembershipEntity):
    organization = models.CharField('Organization Name', help_text='e.g. Mounds View High School', max_length=50)
    authorized_at = models.DateField('Date Authorized', help_text='When did the board approve this team?')

    # This tells us which fields have been modified so custom save methods
    # and signal handlers can do less work.
    tracker = FieldTracker()

MAXIMUM_HOUSEHOLD_MEMBERS = 2
class Household(MembershipEntity):
    dues_plan = models.ForeignKey('DuesPlan', on_delete=models.SET_NULL, blank=True, null=True)
    discount = models.ForeignKey('Discount', on_delete=models.SET_NULL, blank=True, null=True)
    auto_renew = models.BooleanField(default=False)
    external_customer_identifier = models.CharField(max_length=100)
    external_subscription_identifier = models.CharField(max_length=100)

    # This tells us which fields have been modified so custom save methods
    # and signal handlers can do less work.
    tracker = FieldTracker()

    def has_vacancy_for(self, person):
        max_members = MAXIMUM_HOUSEHOLD_MEMBERS
        if (self.discount and not self.discount.allow_family_memberships):
            max_members = 1
        return self.person_set.exclude(pk=person.id).count() < max_members

    def __eligible_for_discount(self):
        # This is America: everyone is eligible to pay full price
        if not self.discount:
            return True
        return self.person_set.count() <= 1

    def clean(self):
        if not self.__eligible_for_discount():
            raise ValidationError({
                'discount': 'Multiperson households are not eligible for this discount.'
            })
        return super().clean()

### Invitations allow someone to add a new person to a household or team they
### manage.
class Invitation(BaseEntity):
    given_name = models.CharField('First Name', max_length=100)
    family_name = models.CharField('Last Name', max_length=100)
    email = models.EmailField('Email Address')
    accepted_at = models.DateTimeField(blank=True, null=True)
    household = models.ForeignKey('Household', null=True, blank=True, on_delete=models.SET_NULL)
    student_team = models.ForeignKey('StudentTeam', null=True, blank=True, on_delete=models.SET_NULL)

    # This tells us which fields have been modified so custom save methods
    # and signal handlers can do less work.
    tracker = FieldTracker()
