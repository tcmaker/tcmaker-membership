from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Person, Household, Discount, DuesPlan, StudentTeam

class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        exclude = ['notes']
        read_only_fields = [
            'created_at',
            'updated_at',
            'keyfob_code',
        ]

class HouseholdSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Household
        exclude = ['notes']
        read_only_fields = [
            'created_at',
            'updated_at',
            'keyfob_code',
        ]

class StudentTeamSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = StudentTeam
        exclude = ['notes']
        read_only_fields = [
            'created_at',
            'updated_at',
        ]

class DuesPlanSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = DuesPlan
        exclude = ['notes']
        read_only_fields = [
            'created_at',
            'updated_at',
        ]

class DiscountSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Discount
        exclude = ['notes']
        read_only_fields = [
            'created_at',
            'updated_at',
        ]
