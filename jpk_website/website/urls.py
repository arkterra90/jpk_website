from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'website'

urlpatterns = [
    path("", views.index, name="index"),
    path("resume/", views.resume, name="resume"),
    path("projects/", views.projects, name="projects"),
    path("blogHome/", views.blogHome, name="blogHome"),
    path("blogPost/<int:postID>/", views.blogPost, name="blogPost"),
    path("subscribe", views.subscribe, name="subscribe")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)