from rest_framework import serializers
from .models import Incentive

class IncentivesSerializer(serializers.ModelSerializer):
    class Meta():
        model = Incentive
        fields = '__all__'