from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Notice
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # 로그인 여부 확인, 접근가능한 유저인지 확인
# 공지사항 목록
class NoticeList(ListView):
    model = Notice
    template_name = 'notice/notice.html'
    ordering = '-pk'
    paginate_by = 3 # 한 페이지에 10개씩 보여주기

# def notice(request):
#     notices = Notice.objects.all().order_by('-pk') # 최신순으로 가져오기
#     return render(
#         request,
#         'notice/notice.html',
#         {
#             'notice_lists': notices,
#         }
#     )
# 공지사항 디테일
class NoticeDetail(DetailView):
    model = Notice


# def notice_page(request, pk):
#     notice = Notice.objects.get(pk=pk)
#
#     return render(
#         request,
#         'notice/notice_detail.html',
#         {
#             'notice': notice,
#         }
#     )

# Create your views here.
# 공지사항 작성 # 로그인 확인, 유저 등급 확인, 작성뷰
class NoticeCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Notice
    fields = ['title', 'content']

    def test_func(self): # 로그인 했는지 혹은 스탭인지 확인
        return self.request.user.is_authenticated or self.request.user.is_staff

    # 로그인 여부 확인
    def form_valid(self, form):
        current_user = self.request.user #
        # 로그인 상태이면서 스탭이거나 관리자인지 확인
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user # 로그인 상태라면 author에 현재 로인한 사용자의 이름 넣기
            return super(NoticeCreate, self).form_valid(form)
        else:
            return redirect('/notice/')

# 위에서 만든 NoticeList를 상속받아 NoticeSearch를 만들면 NoticeList에서 개발한 기능을
# 그대로 이용할 수 있다.

class NoticeSearch(NoticeList):
    paginate_by = None

    def get_queryset(self): # == Notice.objects.all() 과 같음
        q = self.kwargs['q']
        notice_list = Notice.objects.filter(
            Q(title__contains=q)).distinct()
        return notice_list

    # def get_context_data(self, **kwargs):
    #     context = super(NoticeSearch, self).get_context_data()
    #     q = self.kwargs['q']
    #     context['search_info'] = f'검색 결과:{q} ({self.get_queryset().count()})'
    #     return context
        
