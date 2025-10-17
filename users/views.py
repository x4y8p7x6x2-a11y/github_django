from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages


def register(request):
    """회원가입"""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            messages.error(request, "비밀번호가 일치하지 않습니다.")
            return render(request, "users/register.html")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "이미 존재하는 사용자명입니다.")
            return render(request, "users/register.html")
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        login(request, user)
        messages.success(request, "회원가입이 완료되었습니다.")
        return redirect("memo_list")
    
    return render(request, "users/register.html")


def user_login(request):
    """로그인"""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"{username}님, 환영합니다!")
            return redirect("memo_list")
        else:
            messages.error(request, "사용자명 또는 비밀번호가 올바르지 않습니다.")
    
    return render(request, "users/login.html")


def user_logout(request):
    """로그아웃"""
    logout(request)
    messages.success(request, "로그아웃되었습니다.")
    return redirect("login")
