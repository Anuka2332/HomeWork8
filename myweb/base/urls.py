from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('article1/', views.article1, name='article1'),
    path('article2/', views.article2, name='article2'),
    path('article3/', views.article3, name='article3'),
    path('profile/', views.profile, name='profile')

#     path('contact', views.contact, name='contact')
]

