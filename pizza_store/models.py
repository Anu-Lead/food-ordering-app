from django import forms
from django.db import models


class Size(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Swallow(models.Model):
    Swallow_Type = (
        ('A', 'Amala'),
        ('S', 'Semo'),
        ('PY', 'Pounded Yam'),
        ('W', 'Wheat'),
        ('E', 'Eba')
    )
    swallow_type = models.Choices


class Pizza(models.Model):
    swallow = models.ForeignKey(Swallow, on_delete=models.CASCADE)
    # swallow = models.CharField(max_length=100)
    soup = models.CharField(max_length=100)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=20)
