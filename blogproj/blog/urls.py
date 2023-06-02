from django.urls import path
from . import views  # import all views from current directory

# without comma, it will throw an error
urlpatterns = [
    path('', views.home, name='blog-home'),  # empty string means home page
    path('about/', views.about, name='blog-about'),

]
