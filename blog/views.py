from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import NewPost

from taggit.models import Tag


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def post_list(request, tag_slug=None):
    posts = Post.published.all()
    tag = None
    most_visited = Post.objects.all().annotate(most_visited=Count("visited")
                                               ).order_by("most_visited", "-publish")[:3]
    most_tags = Post.tags.most_common()[:3]

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts,
        'tag': tag,
        'most_visited': most_visited,
        'most_tags': most_tags,

    }

    return render(request, 'blog/post/index.html', context)


# class PostDetail(DetailView):
#     model = Post
#     template_name = 'blog/post/detail.html'
#     context_object_name = 'post'


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day,
                             slug=slug,
                             )
    post.visited += 1
    post.save()
    most_visited = Post.objects.all().annotate(most_visited=Count("visited")
                                               ).order_by("most_visited", "-publish")[:3]
    most_tags = Post.tags.most_common()[:3]

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids)\
                                  .exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags'))\
        .order_by('-same_tags', '-publish')[:3]

    context = {
        'post': post,
        'most_visited': most_visited,
        'similar_posts': similar_posts,
        'most_tags': most_tags,
    }
    return render(request, 'blog/post/detail.html', context)

@login_required
def post_new(request):
    form = NewPost(initial={'author':request.user})
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('blog:index')

    return render(request, 'blog/post/new.html', {'form':form})

@login_required
def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    form = NewPost(instance=post)
    if request.method == 'POST':
        form = NewPost(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('blog:index')

    return render(request, 'blog/post/new.html', {'form':form})
