from django import forms

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]  # Указываем только поле контента



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class SearchForm(forms.Form):
    query = forms.CharField(label="Поиск", max_length=255)
