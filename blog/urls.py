from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('posts/', views.post_list, name='posts'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/',
         views.PostDetail.as_view(), name='post_detail'),

    path('tag/<slug:tag_slug>/', views.post_list, name='posts_by_tag'),

]
