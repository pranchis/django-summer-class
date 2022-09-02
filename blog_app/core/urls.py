from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
                  # index
                  path('', index, name='index'),
                  path('login/', user_login, name='login'),
                  path('query/', query, name='query'),
                  path('logout/', log_out, name='logout'),
                  path('register/', user_register, name='register'),
                  # for blog
                  path('blog/create', blog_create, name='blog_create'),
                  path('blogs', blogs_read, name='blogs'),
                  path('blog/<int:pk>/update', blog_update, name='blog_update'),
                  path('blog/<int:pk>/delete', blog_delete, name='blog_delete'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
