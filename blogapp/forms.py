from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput

from .models import Post

class WriteBlog(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

        widgets = {
            'title': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Blog title'
                }),
            'text': forms.Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 3000px;',
                'placeholder': 'Type blog content here..'
                }),
        }
