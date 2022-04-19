from django.shortcuts import render
from .models import Notice

def notice(request):
    notices = Notice.objects.all().order_by('-pk') # 최신순으로 가져오기

    return render(
        request,
        'notice/notice.html',
        {
            'notices': notices,
        }
    )

def notice_page(request, pk):
    notice = Notice.objects.get(pk=pk)

    return render(
        request,
        'notice/notice_detail.html',
        {
            'notice': notice,
        }
    )

# Create your views here.
