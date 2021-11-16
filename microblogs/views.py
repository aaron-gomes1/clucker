from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from .forms import LogInForm, SignUpForm, PostForm, UserListForm
from .models import User, Post
from django.urls import reverse
from .helpers import login_prohibited

@login_required
def follow_toggle(request, user_id):
    current_user = request.user
    try:
        followee = User.objects.get(id=user_id)
        current_user.toggle_follow(followee)
    except ObjectDoesNotExist:
        return redirect('users')
    else:
        return redirect('show_user', user_id=user_id)

def new_post(request):

    if request.user.is_authenticated == False:
        redirect('feed')

    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save(request.user)
        return redirect('feed')

    form = PostForm()
    return render(request, 'new_post.html', {'form' : form})

@login_required
def show_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        posts = Post.objects.filter(author=user)
        following = request.user.is_following(user)
        followable = (request.user != user)
    except ObjectDoesNotExist:
        return redirect('users')
    else:
        return render(request, 'show_user.html', {'user': user, 'posts': posts, 'following': following, 'followable': followable})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

@login_prohibited
def home(request):
    return render(request, 'home.html')

@login_required
def feed(request):
    form = PostForm()
    current_user = request.user
    posts = Post.objects.filter(author=current_user)
    return render(request, 'feed.html', {'form': form, 'posts': posts,'user': current_user})

def log_out(request):
    logout(request)
    return redirect('home')

@login_prohibited
def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        next = request.POST.get('next') or ''
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = next or 'feed'
                return redirect(redirect_url)
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    else:
        next = request.GET.get('next') or ''
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form, 'next': next})

@login_prohibited
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
