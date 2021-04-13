from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser
from post_app.models import ImageModel


class Profile(AbstractUser):
    display_name = models.CharField(max_length=75, null=True, blank=True)
    profile_pic = models.ImageField(upload_to='images/')
    dob = models.DateField(null=True, blank=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    bio = models.CharField(max_length=300)
    following = models.ManyToManyField("self", symmetrical=False, blank=True)
    likes = models.ManyToManyField(
        ImageModel,
        blank=True,
        related_name="likes"
    )  # Ana


def __str__(self):
    return self.display_name
