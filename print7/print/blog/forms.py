from django import forms
from .models import Post
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField


class PostCreateForm(forms.ModelForm):
    content = RichTextField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'tag']
