from django import forms
from .models import Post

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author','title', 'description', 'thumbnail', 'slug', 'body', 'tags', 'status']

