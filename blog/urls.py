from django.urls import path
from .views import Post_list

urlpatterns = [
    path('posts/', Post_list)
]
