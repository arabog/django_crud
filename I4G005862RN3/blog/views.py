from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import Post



class PostListView(generic.ListView):
    model = Post


class PostCreateView(generic.CreateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('blog:all')


class PostDetailView:
    model = Post


class PostUpdateView:
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)


class PostDeleteView:
    model = Post
    fields = “__all__”
    success_url  = reverse_lazy(“blog:all”)


    