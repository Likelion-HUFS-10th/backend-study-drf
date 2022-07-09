from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('', get_all_blogs),
    path('post', post_one_blog),
    path('<int:pk>/', get_one_blog),
    path('put/<int:pk>/', put_one_blog),
    path('delete/<int:pk>/', delete_one_blog),
]