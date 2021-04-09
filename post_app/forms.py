# NEW
from django import forms
from post_app.models import ImageModel

class ImageModelForm(forms.ModelForm):

    class Meta:
        model = ImageModel
        fields = [
            'image_file',
            'caption',
            'author',
            'capture_location',
            'creation_time',
            ]