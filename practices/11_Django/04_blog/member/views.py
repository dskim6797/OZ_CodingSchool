from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as django_login
from django.shortcuts import redirect, render
from django.urls import reverse

def sign_up(request):
    # username = request.POST.get('username')
    # pawword1 = request.POST.get('password1')
    # pawword2 = request.POST.get('password2')
    # print(f"ID: {username}, PW1: {pawword1}, PW2: {pawword2}")

    # username 중복 확인 작업
    # 패스워드 맞는지, 패스워드 정책에 위배되지 않는지(대소문자, 8자이상, ...)
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(settings.LOGIN_URL)

    context = {
        'form':form
    }
    return render(request,'registration/signup.html',context)

def login(request):
    form = AuthenticationForm(request, request.POST or None)

    if form.is_valid():
        django_login(request, form.get_user())

        next = request.GET.get('next')
        if next:
            return redirect(next)

        return redirect(reverse('blog_list'))

    context = {
        'form':form
    }
    return render(request,'registration/login.html',context)