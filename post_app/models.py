from django.db import models
from django.utils import timezone

class ImageModel(models.Model):
    image_file = models.ImageField(upload_to = 'images/')
    caption = models.CharField(max_length=50, blank=True, null=True)
    author = models.ForeignKey(
        "instaUser_app.Profile",
        on_delete=models.CASCADE
    )  # A
    capture_location = models.CharField(max_length=100, blank=True, null=True)
    creation_time = models.DateTimeField(default=timezone.now)
    liked = models.ManyToManyField(
        "instaUser_app.Profile",
        blank=True,
        related_name="liked"
    )  # A

    def __str__(self):
        return f'{self.caption} by {self.author.display_name}'
