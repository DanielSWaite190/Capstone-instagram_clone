from django.db import models
from django.utils import timezone
from instaUser_app.models import Profile

class ImageModel(models.Model):
    image_file = models.ImageField(upload_to = 'images/')
    caption = models.CharField(max_length=50, blank=True, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    capture_location = models.CharField(max_length=100, blank=True, null=True)
    creation_time = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0) 

    def __str__(self):
        return f'{self.caption} by {self.author.display_name}'
