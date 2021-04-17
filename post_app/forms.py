# NEW
from django import forms
from post_app.models import ImageModel
from instaUser_app.models import Profile


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = [
            'image_file',
            'caption',
            'author'
        ]
        widgets = {
            'author': forms.HiddenInput(),
        }  # a.r.t.

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user")
        super(ImageModelForm, self).__init__(*args, **kwargs)
        self.fields["author"].queryset = Profile.objects.filter(username=self.user)
