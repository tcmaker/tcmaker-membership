import django_filters
from .models import Person, Household, StudentTeam

PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Person
        fields = {
            'given_name': ['exact', 'iexact'],
            'family_name': ['exact', 'iexact'],
            'email_name': ['exact', 'iexact'],
            'keyfob_code': ['exact'],
        }
