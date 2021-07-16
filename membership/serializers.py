from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Person, Household, DuesPlan, StudentTeam

from keyfobs.models import KeyfobSerializer

class HouseholdSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Household
        exclude = ['notes']
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

class StudentTeamSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = StudentTeam
        exclude = ['notes']
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

class PersonSerializer(HyperlinkedModelSerializer):
    administered_households = HouseholdSerializer(many=True, read_only=True, source='administered_household_set')
    administered_student_teams = StudentTeamSerializer(many=True, read_only=True, source='administered_studentteam_set')
    keyfobs = KeyfobSerializer(many=True, read_only=True, source='keyfob_set')
    class Meta:
        model = Person
        exclude = ['notes']
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]

class DuesPlanSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = DuesPlan
        exclude = ['notes']
        read_only_fields = [
            'id',
            'created_at',
            'updated_at',
        ]
