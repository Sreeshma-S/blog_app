from urllib import request
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from rest_framework import generics
from .serializers import BlogSerializer
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from .forms import WriteBlog
from django.shortcuts import redirect
# from celery.schedules import crontab
# from celery.task import periodic_task
# from .tasks import publish_scheduled_posts


# Create your views here.
class BlogListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class BlogCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class BlogUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

class BlogDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(print("Blog Deleted"))

def blog_list(request):
    User = get_user_model()
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blogapp/blog_list.html', {'posts': posts})

from django.contrib.auth import get_user_model
def blog_new(request, user):
    if request.method == "POST":
        form = WriteBlog(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            User = get_user_model()
            user_qs = User.objects.filter(username=user)
            post.author = user_qs[0]
            post.published_date = timezone.now()
            post.save()
            return redirect('blogapp:blog_view', pk=post.pk)
    else:
        form = WriteBlog()
    return render(request, 'blogapp/blog_edit.html', {'form': form})

def blog_edit(request, pk):
    blog = get_object_or_404(Post, pk=pk)

    if request.method != 'POST':
        form = WriteBlog(instance=blog)

    else:
        form = WriteBlog(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogapp:blogs')


    context = {'post': blog, 'form': form}
    return render(request, 'blogapp/blog_edit.html', context)

def blog_detail(request, pk):
    detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/blog_detail.html', {'detail': detail})

def blog_delete(request, pk):
    blog = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('blogapp:blogs')
    return render(request, 'blogapp/blog_delete.html', {'blog':blog.title})


# @periodic_task(run_every=(crontab(hour=x, minute=y)))
# def schedule_publishing():
#     publish_scheduled_posts.delay()
