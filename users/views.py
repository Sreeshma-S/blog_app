from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            # messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('blogapp:blogs', user = username)
            # return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    # return render(request, 'users/profile.html')
    return redirect('blogapp:blogs', user = request.user)
