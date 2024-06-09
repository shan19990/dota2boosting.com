from django.urls import path
from .views import BoosterListCreate, BoosterRetrieveUpdateDestroy


urlpatterns = [
    path('', BoosterListCreate.as_view(), name='booster-list-create'),
    path('<int:pk>/', BoosterRetrieveUpdateDestroy.as_view(), name='booster-retrieve-update-destroy'),
]


