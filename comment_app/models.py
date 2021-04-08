from django.db import models
from instaUser_app.models import Profile
from post_app.models import ImageModel

class Comment(models.Model):
    owner = models.OneToOneField(Profile, on_delete=models.CASCADE)
    # Image = models.OneToOneField(ImageModel, on_delete=models.CASCADE)
    comment = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.owner.username}: {self.comment}'
