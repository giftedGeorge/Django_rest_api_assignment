from django.forms import ValidationError
from rest_framework import serializers
from inventory_api.models import Computer

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = "__all__"

    def validate_number_of_cores(self, value):
        options = [1,2,4,8]
        if value not in options:
            raise ValidationError("number_of_cores must be either 1,2,4, or 8")
        return value