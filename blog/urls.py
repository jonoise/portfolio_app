from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='index'),
    # path('<int:year>/<int:month>/<int:day>/<str:slug>/',
    #      views.PostDetail.as_view(), name='post_detail'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/',
         views.post_detail, name='post_detail'),
    path('tag/<slug:tag_slug>/', views.post_list, name='posts_by_tag'),
    path('new/', views.post_new, name='post_new'),
    path('edit/<str:pk>', views.post_edit, name='post_edit'),

]
