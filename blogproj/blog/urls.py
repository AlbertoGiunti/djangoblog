from django.urls import path
from . import views  # import all views from current directory
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


# without comma, it will throw an error
urlpatterns = [
    # path('', views.home, name='blog-home'),  # empty string means home page

    path('about/', views.about, name='blog-about'),
    path('', PostListView.as_view(), name='blog-home'),  # empty string means home page
    path('post/new/', views.PostCreateView.as_view(), name='blog-new'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='blog-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='blog-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='blog-delete'),
]
