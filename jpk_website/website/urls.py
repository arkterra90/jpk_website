from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path("", views.index, name="index"),
    path("resume/", views.resume, name="resume"),
    path("projects/", views.projects, name="projects"),
    path("blogHome/", views.blogHome, name="blogHome"),
    path("blogPost/<int:postID>/", views.blogPost, name="blogPost"),
    path("subscribe", views.subscribe, name="subscribe")
]