from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Memo


@login_required
def memo_list(request):
    """메모 목록 조회"""
    memos = Memo.objects.filter(user=request.user)
    return render(request, "memos/memo_list.html", {"memos": memos})


@login_required
def memo_detail(request, pk):
    """메모 상세 조회"""
    memo = get_object_or_404(Memo, pk=pk, user=request.user)
    return render(request, "memos/memo_detail.html", {"memo": memo})


@login_required
def memo_create(request):
    """메모 생성"""
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        if title and content:
            Memo.objects.create(
                user=request.user,
                title=title,
                content=content
            )
            messages.success(request, "메모가 생성되었습니다.")
            return redirect("memo_list")
        else:
            messages.error(request, "제목과 내용을 모두 입력해주세요.")
    
    return render(request, "memos/memo_form.html")


@login_required
def memo_update(request, pk):
    """메모 수정"""
    memo = get_object_or_404(Memo, pk=pk, user=request.user)
    
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        
        if title and content:
            memo.title = title
            memo.content = content
            memo.save()
            messages.success(request, "메모가 수정되었습니다.")
            return redirect("memo_detail", pk=memo.pk)
        else:
            messages.error(request, "제목과 내용을 모두 입력해주세요.")
    
    return render(request, "memos/memo_form.html", {"memo": memo})


@login_required
def memo_delete(request, pk):
    """메모 삭제"""
    memo = get_object_or_404(Memo, pk=pk, user=request.user)
    
    if request.method == "POST":
        memo.delete()
        messages.success(request, "메모가 삭제되었습니다.")
        return redirect("memo_list")
    
    return render(request, "memos/memo_confirm_delete.html", {"memo": memo})
