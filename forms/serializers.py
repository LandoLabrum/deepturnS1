from rest_framework import serializers
from .models import F101
from rest_framework import generics
from leads.models import Leads

class F101Serializer(serializers.ModelSerializer):
    class Meta:
        model = F101
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'