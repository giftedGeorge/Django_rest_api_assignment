from random import choices
from django.db import models
from django.forms import JSONField
from multiselectfield import MultiSelectField


port_type_choices = (('1','vga'), ('2','hdmi'), ('3','optical'))

# Create your models here.
class Computer(models.Model):
    brand = models.CharField(max_length=100)
    processor_speed = models.DecimalField(max_digits=5, decimal_places=2)
    number_of_cores = models.IntegerField()
    number_of_usb_ports = models.IntegerField()
    number_of_hdmi_ports = models.IntegerField()

    def __str__(self):
        return self.brand


class Mouse(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)

    def __str__(self):
        return self.brand



class Keyboard(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    colour = models.CharField(max_length=100)
    has_numeric_keypad = models.CharField(max_length=100)
    has_backlight = models.CharField(max_length=100)

    def __str__(self):
        return self.brand



class Monitor(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    screen_resolution = models.CharField(max_length=100)   
    port_types = MultiSelectField(max_length=20 , choices=port_type_choices, max_choices=3)

    def __str__(self):
        return self.brand

