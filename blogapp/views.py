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
from django.contrib.auth.models import User

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

def blog_list(request, user):
    posts = Post.objects.filter(date__lte=timezone.now()).order_by('date')
    return render(request, 'blogapp/blog_list.html', {'posts': posts, 'user': user})

def blog_detail(request, pk):
    detail = get_object_or_404(Post, pk=pk)
    return render(request, 'blogapp/blog_detail.html', {'detail': detail})


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