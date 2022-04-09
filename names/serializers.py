from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model = Person
        fields = ('__all__') # all fields required