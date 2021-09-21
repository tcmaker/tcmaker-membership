from rest_framework import serializers
from .models import Keyfob

class KeyfobSerializer(serializers.HyperlinkedModelSerializer):
    is_membership_valid = serializers.BooleanField(source='compute_is_membership_valid', required=False)
    membership_valid_through = serializers.DateTimeField(source='compute_membership_valid_through', required=False)

    class Meta:
        model = Keyfob
        exclude = ['notes']
        read_only_fields = [
            'created_at',
            'updated_at',
            'is_membership_valid',
            'membership_valid_through',
        ]
