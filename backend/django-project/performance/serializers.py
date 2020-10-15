from rest_framework import serializers
from .models import Vara, VaraList


class VaraListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaraList
        fields = ['vara_id', 'name']

class VaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vara
        fields = ['vara_id',
                  'name',
                  'ranking',
                  'finished_processes',
                  'movements',
                  'group_id',
                  'time_macrostep_1',
                  'time_macrostep_2',
                  'time_macrostep_3',
                  'time_macrostep_4',
                  'days_finish_process',
                  'latitude',
                  'longitude']
