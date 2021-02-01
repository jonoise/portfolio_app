from django.urls import path
from . import views

app_name = 'frontend'
urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path("what's-next/", views.next, name='next'),
    path("thank-you/", views.thank_you, name='thankyou'),
]
