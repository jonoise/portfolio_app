from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

# Create your views here.


class PostList(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_detail(request):
    pass


def post_delete(request):
    pass
