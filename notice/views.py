from django.shortcuts import render, redirect
from .models import Notice
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # 로그인 여부 확인, 접근가능한 유저인지 확인
# 공지사항 목록
class NoticeList(ListView):
    model = Notice
    template_name = 'notice/notice.html'
    ordering = '-pk'


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
# 공지사항 작성
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
