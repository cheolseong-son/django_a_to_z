from django.shortcuts import render
from .models import Post

def index(request): # 장고 기본제공 함수 render를 사용해 템플릿 폴더에서 index.html파일을 찾아 방문자에게 보여줌
    posts = Post.objects.all().order_by('-pk')  # views.py에서 데이터베이스에 쿼리를 날려 원하는 레코드를 가져올 수 있다.
    # .order_by('-pk') : 최신순으로 정렬하여 가져옴
    return render(
        request,
        'blog/index.html',
        {
            'posts':posts
        }

    )
# Create your views here.
