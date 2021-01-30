from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from taggit.models import Tag

# Create your views here.


def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    context = {
        'posts': posts,
        'tag': tag,
    }

    return render(request, 'blog/post/list.html', context)


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post/detail.html'
    context_object_name = 'post'


def post_delete(request):
    pass
