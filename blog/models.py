import imp
from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
import os
from markdownx.utils import markdown  # 마크다운 내용 그대로 페이지에 보이도록 하기


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


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'


class Post(models.Model):

    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = MarkdownxField()

    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    # 사용자가 작한 모든 것이 삭제됨
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 사용자가 작성한 글은 남고 작성자명을 빈칸으로
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # Post에 카테고리 필드 추가, blank= True : 카테고리를 빈 칸으로 지정할 수 있음
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author}'

    # Post 레코드의 content 필등에 저장되어 있는 텍스트를 마크다운 문법을 적용해 HTML로 만든다.
    def get_content_markdown(self):
        return markdown(self.content)

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author}::{self.content}'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}'

    # 구글 로그인은 구글 아바타가 나오고 아니면 그냥 회색
    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://doitdjango.com/avatar/id/855/04bb6400255104ea/svg/{ self.author.email }.png/'
