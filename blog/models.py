from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User

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
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=250, verbose_name='title')
    slug = models.SlugField(max_length=250, unique_for_date='created')
    body = models.TextField()

    objects = models.Manager()
    draft = DraftManager()
    published = PublishedManager()

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
        return reverse("blog:post_detail", kwargs={
            "year": self.publish.year,
            "month": self.publish.month,
            "day": self.publish.day,
            "slug": self.slug
        })
