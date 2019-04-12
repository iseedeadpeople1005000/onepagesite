from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _
from . import models
from django.contrib.auth import get_user_model
User = get_user_model()



class CommentForm(ModelForm):
    class Meta():
        model = models.Comment
        fields = ["Comment_Text", "Comment_Author"]
        widgets = {
                    'Comment_Text': Textarea(attrs={
                       'id': 'Comment_Text',
                       'rows': 3,
                       'cols': 50,
                       "maxlength": 150,
                       'required': True,
                       'placeholder': 'Ваш комментарий'}),
                    'Comment_Author': Textarea(attrs={
                       'id': 'Comment_Author',
                       'rows': 1,
                       'cols': 25,
                       "maxlength": 25,
                       'required': True,
                       'placeholder': 'Ваше имя'})}