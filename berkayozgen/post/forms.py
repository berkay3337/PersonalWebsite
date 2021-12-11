from django import forms
from django.db.models import fields
from .models import Post, Comment
from captcha.fields import ReCaptchaField

class PostForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Post
        fields = [
            'title',
            'post_content',
            'image',          
        ]

class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()
    class Meta:
        model = Comment
        fields = {
            'content',
            'name',
           
            
        }