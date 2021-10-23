from rest_framework import serializers
from .models import one
from rest_framework import generics
# from lead.models import lead_model

class one_serializer(serializers.ModelSerializer):
    class Meta:
        model = one
        fields = '__all__'
