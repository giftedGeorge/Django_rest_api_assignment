from django.db import models

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
