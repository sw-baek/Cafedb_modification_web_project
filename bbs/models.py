from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.CharField('작성자', max_length=20, unique=True)
    contents = models.TextField('내용', max_length=500, unique=True)
    created_date = models.DateTimeField('작성일', auto_now_add=True)

    def __str__(self):
        return self.contents

