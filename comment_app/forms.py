from django import forms
from comment_app.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        
        fields = [
            'text'
        ]

        labels = {
            'text':'Comment'
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['placeholder'] = 'Comment Here'
