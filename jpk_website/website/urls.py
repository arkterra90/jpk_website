from django.urls import path
from django_distill import distill_path
from . import views
from .models import BlogEntry

app_name = 'website'

# Function to dynamically generate blog post IDs for static site generation
def get_blog_post_ids():
    # Fetch IDs of all blog entries and return as a list of tuples
    from .models import BlogEntry
    return [(blog_id,) for blog_id in BlogEntry.objects.values_list('id', flat=True)]


urlpatterns = [
    distill_path("", views.index, name="index", distill_file="index.html"),  # Home page
    distill_path("resume/", views.resume, name="resume", distill_file="resume.html"),  # Resume page
    distill_path("projects/", views.projects, name="projects", distill_file="projects.html"),  # Projects page
    distill_path("blogHome/", views.blogHome, name="blogHome", distill_file="blogHome.html"),  # Blog home page
    distill_path(
        "blogPost/<int:postID>/", 
        views.blogPost, 
        name="blogPost", 
        distill_func=get_blog_post_ids
    ),  # Blog post detail
    path("subscribe", views.subscribe, name="subscribe"),  # Subscription (dynamic, not static)
]
