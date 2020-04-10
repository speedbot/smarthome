from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
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


class Device(TimeStampMixin, models.Model):
    class Meta:
        abstract = True
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
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


class Fan(Device):
    speed = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
