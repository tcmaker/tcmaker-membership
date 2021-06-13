from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from membership import serializers, models
from keyfobs.models import Keyfob
from keyfobs.serializers import KeyfobSerializer

class PersonViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filterset_fields = ['given_name', 'family_name', 'email', 'keyfob_code']

class HouseholdViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.Household.objects.all()
    serializer_class = serializers.HouseholdSerializer
    filterset_fields = ['status', 'name']

class StudentTeamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.StudentTeam.objects.all()
    serializer_class = serializers.StudentTeamSerializer
    filterset_fields = ['status', 'name']

class DuesPlanViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = models.DuesPlan.objects.all()
    serializer_class = serializers.DuesPlanSerializer

class KeyfobViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Keyfob.objects.all()
    serializer_class = KeyfobSerializer
