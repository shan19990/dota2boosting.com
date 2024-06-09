# serializers.py

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Wallet, Transaction

class WalletTransactionUpdateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    balance_change = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField()

    def update_wallet_transaction(self):
        user_id = self.validated_data.get('user_id')
        balance_change = self.validated_data.get('balance_change')
        description = self.validated_data.get('description')

        user = User.objects.get(id=user_id)

        # Create wallet if it does not exist
        wallet, created = Wallet.objects.get_or_create(user=user)

        # Update the wallet balance
        wallet.balance += balance_change

        # Update total deposit if balance change is positive
        if balance_change > 0:
            wallet.total_deposit += balance_change

        # Update perks based on total_deposit
        if wallet.total_deposit >= 1000:
            wallet.perk = 'platinum'
        elif wallet.total_deposit >= 500:
            wallet.perk = 'diamond'
        elif wallet.total_deposit >= 250:
            wallet.perk = 'gold'
        elif wallet.total_deposit >= 100:
            wallet.perk = 'silver'
        elif wallet.total_deposit > 0:
            wallet.perk = 'bronze'
        else:
            wallet.perk = ''

        wallet.save()

        # Create a new transaction
        transaction = Transaction.objects.create(
            wallet=wallet,
            balance=wallet.balance,
            change=balance_change,
            description=description
        )

        return transaction
