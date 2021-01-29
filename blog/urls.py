from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('posts/', views.PostList.as_view(), name='posts'),
    path('<int:year>/<int:month>/<int:day>/<str:slug>/',
         views.PostDetail.as_view(), name='post_detail')
]
