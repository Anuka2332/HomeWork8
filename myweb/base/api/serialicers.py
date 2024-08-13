from rest_framework.serializers import ModelSerializer

from ..models import Certif


class CertifSerializer(ModelSerializer):
    class Meta:
        model = Certif
        fields = '__all__'

