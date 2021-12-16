from rest_framework import serializers
from .models import testmodel

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = testmodel
        exclude = []
        