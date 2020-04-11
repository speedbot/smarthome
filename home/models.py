from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone

from colorful.fields import RGBColorField


class TimeStampMixin(models.Model):
    class Meta:
        abstract = True
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)


class DeviceManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at=None)
    def unlimited(self):
        return super().get_queryset()


class Device(TimeStampMixin, models.Model):
    class Meta:
        unique_together = ('owner', 'name')
        abstract = True
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    state = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(default=None, null=True)
    objects = DeviceManager()

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()


class Bulb(Device):
    brightness = models.IntegerField(
        default=10,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    color = RGBColorField()

    def get_absolute_url(self):
        return '/bulb/detail/{}/'.format(self.id)


class Fan(Device):
    speed = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )

    def get_absolute_url(self):
        return '/fan/detail/{}/'.format(self.id)