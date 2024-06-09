from rest_framework import serializers
from .models import MMRBoostingJob, Coaching, BehaviousScore, LowPriority, BattleCup,NormalWins

class MMRBoostingJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = MMRBoostingJob
        fields = '__all__'

class CoachingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coaching
        fields = '__all__'

class BehaviousScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BehaviousScore
        fields = '__all__'

class LowPrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = LowPriority
        fields = '__all__'

class BattleCupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BattleCup
        fields = '__all__'

class NormalWinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NormalWins
        fields = '__all__'

class CombinedDataSerializer(serializers.Serializer):
    mmr_boosting_jobs = MMRBoostingJobSerializer(many=True)
    coaching = CoachingSerializer(many=True)
    behaviour_scores = BehaviousScoreSerializer(many=True)
    low_priority = LowPrioritySerializer(many=True)
    battle_cup = BattleCupSerializer(many=True)
    normal_wins = NormalWinsSerializer(many=True)
