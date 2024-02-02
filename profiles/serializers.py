from rest_framework import serializers
from django.conf import settings
from .models import Profile

class PosfilesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ( 'id','email','created_at','updated_at','is_active')
        model = Profile
