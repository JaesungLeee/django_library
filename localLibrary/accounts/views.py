from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from .forms import SignUpForm
# Create your views here.

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        # 가입하기
        username = form.cleaned_data.get('username')   
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)   # cleaned data에서 온 name password 인증  
        login(request, user) # login
        return redirect('index')

    else: 
        form = SignUpForm
    return render(request, 'signup.html', {'form' : form})