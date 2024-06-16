# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.contrib.auth.decorators import login_required
#
from .forms import UserRegForm
# from celery.schedules import crontab
# from celery.task import periodic_task
# from .tasks import publish_scheduled_posts
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# # Create your views here.
#

def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = UserRegForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # return render(request, 'users/profile.html')
    return redirect('blogapp:blogs', user = request.user)
