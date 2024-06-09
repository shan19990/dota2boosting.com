from rest_framework import serializers
from .models import BoosterProfile

class BoosterProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoosterProfile
        fields = ['id', 'name', 'photo', 'rank', 'orders_completed', 'rating', 'boosting_for', 'languages']