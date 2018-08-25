from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        # field to be exposed
        fields = ('title', 'text')
