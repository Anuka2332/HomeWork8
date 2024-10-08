from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('article1/', views.article1, name='article1'),
    path('article2/', views.article2, name='article2'),
    path('article3/<str:id>/', views.article3, name='article3'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('adding/<str:id>/', views.adding, name='adding'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register_page, name='register'),
    path('add/', views.add_book, name='add'),
    path('reading/<str:id>/', views.reading, name='reading'),
    path('delete_certif/<str:id>', views.delete_certif, name='delete_certif'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_comment/<str:id>/', views.delete_comment, name='delete_comment')

]

