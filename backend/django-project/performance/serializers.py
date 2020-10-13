from rest_framework import serializers
from .models import Vara


class VaraSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vara
        fields = ['name', 'latitude', 'longitude']

