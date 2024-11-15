from django.shortcuts import render
from .models import BlogEntry


def index(request):
    return render(request, "website/index.html")

def resume(request):
    return render(request, "website/resume.html")

def projects(request):
    return render(request, "website/projects.html")

def blogHome(request):

    #Queries for all blog entries to give a listing on the blogHome page.
    BlogEntries = BlogEntry.objects.all().order_by('-blogDate')
    Context = {'BlogEntries': BlogEntries}

    return render(request, "website/bloghome.html", Context)
    

def blogPost(request, postID):

    entry = BlogEntry.objects.get(id=postID)
    pass