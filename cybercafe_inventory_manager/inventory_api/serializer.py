from django.forms import ValidationError
from rest_framework import serializers
from inventory_api.models import Mouse
from inventory_api.models import Computer

#for the computer entity
class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = "__all__"

    def validate_number_of_cores(self, value):
        options = [1,2,4,8]
        if value not in options:
            raise ValidationError("number_of_cores must be either 1,2,4, or 8")
        return value


#for the mouse entity
class MouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mouse
        fields = "__all__"

    def validate_type(self, value):
        options = ["wireless","wired"]
        if value not in options:
            raise ValidationError("type must be either wireless or wired")
        return value