from django.db import models

# 데이터베이스에 반영하기 위해서 python manage.py makemigrations --> python manage.py migrate
# No changes detected 는 프로젝트 폴더의 settings.py에 등록이 되어있지 않은 상태
# 등록 : 'blog', 'single_pages' installed_apps에 등록함

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'
# Create your models here.
