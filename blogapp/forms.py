from django import forms

from .models import Post

class WriteBlog(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)