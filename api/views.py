from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from membership import serializers, models

class PersonViewSet(viewsets.ModelViewSet):
    queryset = models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filterset_fields = ['given_name', 'family_name', 'email', 'keyfob_code']

class DiscountViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Discount.objects.all()
    serializer_class = serializers.DiscountSerializer

class HouseholdViewSet(viewsets.ModelViewSet):
    queryset = models.Household.objects.all()
    serializer_class = serializers.HouseholdSerializer
    filterset_fields = ['status', 'name']

class StudentTeamViewSet(viewsets.ModelViewSet):
    queryset = models.StudentTeam.objects.all()
    serializer_class = serializers.StudentTeamSerializer
    filterset_fields = ['status', 'name']

class DuesPlanViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.DuesPlan.objects.all()
    serializer_class = serializers.DuesPlanSerializer
