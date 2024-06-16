from django.urls import path
from . import views
from .views import *
import users
from users.views import register

app_name = 'blogapp'

urlpatterns = [
    path('', users.views.register, name='home'),
    path('home/', views.blog_list, name='blogs'),
    path('blog/view/<int:pk>/', views.blog_detail, name='blog_view'),
    path('blog/<user>/new/', views.blog_new, name='blog_new'),
    path('blog/delete/<int:pk>/', views.blog_delete, name='blog_remove'),
    path('blog/list/', BlogListView.as_view(), name='blog_list'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/edit/<int:pk>/', views.blog_edit, name='blog_edit'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]