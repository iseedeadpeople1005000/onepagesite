from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Comment(models.Model):
    class Meta():
        db_table = "Comment"
    Comment_Text = models.TextField(verbose_name="", max_length=150, default="")
    Comment_Author = models.TextField(verbose_name="", max_length=25, default="")