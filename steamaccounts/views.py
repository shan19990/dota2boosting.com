from rest_framework import generics
from .models import Account
from .serializers import AccountSummarySerializer, AccountDetailSerializer

class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer

class AccountSummaryListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSummarySerializer

class AccountSummaryDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSummarySerializer
