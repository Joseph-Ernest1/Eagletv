from rest_framework import serializers
from .models import News, Contact

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields ="__all__"