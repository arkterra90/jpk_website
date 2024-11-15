from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "website/index.html")

def resume(request):
    return render(request, "website/resume.html")

def projects(request):
    return render(request, "website/projects.html")