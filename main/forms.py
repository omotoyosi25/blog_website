from django import forms
from .models import Post


class BlogComment(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=200)
    message=forms.CharField(widget=forms.Textarea())

class AddPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields = ['title', 'desc', 'article', 'thumbnail', 'category']