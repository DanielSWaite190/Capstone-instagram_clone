from django.db import models
from instaUser_app.models import Profile
from post_app.models import ImageModel
from django.utils import timezone

class Comment(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    image = models.ForeignKey(ImageModel, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    creation_time = models.DateTimeField(default=timezone.now)
    # likes = models.IntegerField(default=0)


    def __str__(self):
        return f'{self.owner.username}: {self.text}'
