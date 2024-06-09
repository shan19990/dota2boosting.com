# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import WalletTransactionUpdateSerializer
from .models import Wallet, Transaction

class WalletTransactionUpdateView(APIView):
    def post(self, request):
        serializer = WalletTransactionUpdateSerializer(data=request.data)

        if serializer.is_valid():
            try:
                transaction = serializer.update_wallet_transaction()
                return Response({
                    'message': 'Wallet and transaction updated successfully',
                    'transaction': {
                        'wallet': transaction.wallet.id,
                        'balance': transaction.balance,
                        'change': transaction.change,
                        'description': transaction.description,
                        'transaction_date': transaction.transaction_date
                    }
                }, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"error": "User does not exist."}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

