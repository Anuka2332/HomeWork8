from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('certifs/', views.get_certifs),
    path('certifs/<str:id>', views.get_certif)

]

