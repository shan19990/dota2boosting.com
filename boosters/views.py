from rest_framework import generics, status
from rest_framework.response import Response
from .models import BoosterProfile
from .serializers import BoosterProfileSerializer

class BoosterListCreate(generics.ListCreateAPIView):
    queryset = BoosterProfile.objects.all()
    serializer_class = BoosterProfileSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoosterRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoosterProfile.objects.all()
    serializer_class = BoosterProfileSerializer
