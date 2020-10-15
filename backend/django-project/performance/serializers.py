from rest_framework import serializers
from .models import Vara, VaraList, StepConfiguration, Comments, Steps


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

class StepConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
      model = StepConfiguration
      fields = ['step_id', 'origin', 'destination']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comments
      fields = ['comment_id', 'comentario']

class StepsSerializer(serializers.ModelSerializer):
    class Meta:
      model = Steps
      fields = ['step_id',
                'vara_id',
                'min_time',
                'med_time',
                'max_time',
                'frequency',
                'comment_id']
