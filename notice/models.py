from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # 사용자가 작한 모든 것이 삭제됨
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 사용자가 작성한 글은 남고 작성자명을 빈칸으로
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/notice/{self.pk}'
