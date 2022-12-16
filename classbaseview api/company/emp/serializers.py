from rest_framework import serializers
from.models import employee

class empserializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields=['name','salary','email']
        