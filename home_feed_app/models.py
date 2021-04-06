from django.db import models
from django.utils import timezone

class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=150)

    def __str__(self):
        return self.username


class Profile(models.Model):
    name = models.CharField(max_length=150)
    about = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    imageModel = models.OneToOneField(ImageModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.owner.username}: {self.comment}'


class ImageModel(models.Model):
    image_file = models.CharField(max_length=150)
    caption = models.CharField(max_length=50, blank=True, null=True)
    user = models.OneToOneField(Useer, on_delete=models.CASCADE)
    capture_location = models.CharField(max_length=100, blank=True, null=True)
    creation_time = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.caption} by {self.User.username}'
