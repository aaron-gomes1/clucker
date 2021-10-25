from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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

def show_user(request, username):
    #reverse('show_user', kwargs={'username': username})
    form = ShowUserForm(User.objects.get(username=username))
    return render(request, 'show_user.html', {'form' : form})
    #return HttpResponse(f'The user is {username}')
    #return render(request, 'show_user.html')

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
    if request.user.is_authenticated == False:
        if request.method == 'POST':
            form = LogInForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('feed')
            # Add error message here
            messages.add_message(request, messages.ERROR, "The credientals provided are invalid")
        form = LogInForm()
        return render(request, 'log_in.html', {'form': form})
    else:
        return redirect('feed')

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
