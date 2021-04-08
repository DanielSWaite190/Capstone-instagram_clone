from django.db import models
from phone_field import PhoneField
from django.contrib.auth.models import AbstractUser

# class User(AbstractUser):
#     display_name = models.CharField(max_length=75, null=True, blank=True)
#     following = models.ManyToManyField("self", symmetrical=False, blank=True)
#
#     def __str__(self):
#         return self.username



# Do we want two models or do we just want to use one???
class Profile(AbstractUser):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=75, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    # profile_pic = models.ImageField(upload_to ='images/')
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length = 254)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    bio = models.CharField(max_length=300)
    following = models.ManyToManyField("self", symmetrical=False, blank=True)
