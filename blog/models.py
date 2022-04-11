from django.db import models
from django.contrib.auth.models import User
import os

# 데이터베이스에 반영하기 위해서 python manage.py makemigrations --> python manage.py migrate
# No changes detected 는 프로젝트 폴더의 settings.py에 등록이 되어있지 않은 상태
# 등록 : 'blog', 'single_pages' installed_apps에 등록함

class Post(models.Model):

    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
# Create your models here.
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

