from django.db import models
from django.contrib.auth.models import User
import os

# 데이터베이스에 반영하기 위해서 python manage.py makemigrations --> python manage.py migrate
# No changes detected 는 프로젝트 폴더의 settings.py에 등록이 되어있지 않은 상태
# 등록 : 'blog', 'single_pages' installed_apps에 등록함

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'
    # categorys로 표기되는 것을 Categories로 변경
    class Meta:
        verbose_name_plural = 'Categories'

class Post(models.Model):

    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # 사용자가 작한 모든 것이 삭제됨
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 사용자가 작성한 글은 남고 작성자명을 빈칸으로
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # Post에 카테고리 필드 추가, blank= True : 카테고리를 빈 칸으로 지정할 수 있음
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'
# Create your models here.
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]

