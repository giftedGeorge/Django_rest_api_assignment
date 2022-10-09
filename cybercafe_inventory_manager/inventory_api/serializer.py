from django.forms import ValidationError
from rest_framework import serializers
from inventory_api.models import Computer, Mouse, Keyboard


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


#for the keyboard entity
class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = "__all__"

    def validate(self, data):
        options = ["yes","no"]
        if data['has_numeric_keypad'] not in options and data["has_backlight"] not in options:
            raise ValidationError("has_numeric_keypad must be either yes or no")
        return data
