from django.shortcuts import render, redirect
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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


def category_page(request, slug):
    if slug =='no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count(),
            'category': category,
        }
    )

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'tag': tag,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),

        }
    )


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

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context



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

# LoginRequiredMixin : 이 클라스를 추가하면 로그인 했을 경우만 정쌍적으로 페이지가 보인다.
class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user # 웹사이트의 방문자
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser): # 웹사이트 방문자가 로그인 상태인지 아닌지 확인
            form.instance.author = current_user # 참이면 form의 (instance)새로 생성한 포스트의 author필드에 current_user 넣기
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/') # 되돌려 보냄

