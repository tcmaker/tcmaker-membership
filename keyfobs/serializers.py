from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Keyfob

class KeyfobSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Keyfob
        exclude = ['notes']
        read_only_fields = [
            'created_at',
            'updated_at',
        ]
