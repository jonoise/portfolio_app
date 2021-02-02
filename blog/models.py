from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class DraftManager(models.Manager):
    def get_queryset(self):
        return super(DraftManager, self).get_queryset().filter(status='draft')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    visited = models.BigIntegerField(
        verbose_name='visited', blank=True, null="True", default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')

    title = models.CharField(max_length=250, verbose_name='title')
    description = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(
        upload_to='media/blog/thumbnails/', blank=True, null=True, default="blog/default_blog.jpg")
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = RichTextField(null=True, blank=True)

    objects = models.Manager()
    draft = DraftManager()
    published = PublishedManager()
    tags = TaggableManager()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.publish.year,
                                                 self.publish.month,
                                                 self.publish.day,
                                                 self.slug])
