from django import forms
#importing models from models.py
from models import User,PostModel,LikeModel,CommentModel

#declaring class for signing up a new user
class SignUpForm(forms.ModelForm):
  class Meta:
    model = User
    fields=['email','username','name','password']           #fields appear on the page

#declaring class for login a already user
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]

#declaring class to post images
class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=['image', 'caption']


#declaring class to like post
class LikeForm(forms.ModelForm):

    class Meta:
        model = LikeModel
        fields=['post']


#declaring class to comment on post
class CommentForm(forms.ModelForm):

    class Meta:
        model = CommentModel
        fields = ['comment_text', 'post']