from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import LogInForm, SignUpForm, PostForm, UserListForm, ShowUserForm
from .models import User
from django.urls import reverse

def new_post(request):

    if request.user.is_authenticated == False:
        redirect('feed')

    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save(request.user)
        return redirect('feed')

    form = PostForm()
    return render(request, 'new_post.html', {'form' : form})

def show_user(request, id):
    form = ShowUserForm(User.objects.get(id=id))
    return render(request, 'show_user.html', {'form' : form})

@login_required
def user_list(request):
    form = UserListForm()
    return render(request, 'user_list.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def feed(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            return redirect('new_post')

        form = PostForm()
        return render(request, 'feed.html', {'form': form})
    else:
        return redirect('log_in')

def log_out(request):
    logout(request)
    return redirect('home')

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = request.POST.get('next') or 'feed'
                return redirect(redirect_url)
        messages.add_message(request, messages.ERROR, "The credientals provided are invalid")
    form = LogInForm()
    next = request.GET.get('next') or ''
    return render(request, 'log_in.html', {'form': form, 'next': next})

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('feed')

    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
