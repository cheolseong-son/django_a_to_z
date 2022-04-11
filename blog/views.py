from django.shortcuts import render
from .models import Post, Category
from django.views.generic import ListView, DetailView

# cbv로 포스트 목록 페이지 만들기
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # template_name = '/blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

# def index(request):
#     posts = Post.objects.all().order_by('-pk')  # views.py에서 데이터베이스에 쿼리를 날려 원하는 레코드를 가져올 수 있음
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )
#

# cbv로 포스트 상세 페이지 만들기
class PostDetail(DetailView):
    model = Post

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post,
#         }
#     )
# Create your views here.
