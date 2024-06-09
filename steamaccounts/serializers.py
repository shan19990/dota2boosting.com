from rest_framework import serializers
from .models import Account

class AccountSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['mmr', 'rank', 'communication', 'behaviour']

class AccountDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
