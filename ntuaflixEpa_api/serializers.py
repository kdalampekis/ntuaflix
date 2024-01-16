from rest_framework import serializers
from .models import TitleBasic

class TitleBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleBasic
        fields = '__all__'  # You can list fields you want to include
