from django.urls import path
from .views import AccountListCreateView, AccountDetailView, AccountSummaryListView, AccountSummaryDetailView

urlpatterns = [
    path('', AccountListCreateView.as_view(), name='account-list-create'),
    path('<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('summary/', AccountSummaryListView.as_view(), name='account-summary-list'),
]
