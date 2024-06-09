from rest_framework import serializers
from .models import Review
from django.contrib.contenttypes.models import ContentType

class ReviewSerializer(serializers.ModelSerializer):
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(), 
        slug_field='model'
    )

    class Meta:
        model = Review
        fields = '__all__'
