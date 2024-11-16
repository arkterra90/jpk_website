from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogEntry
from .forms import SubscriberForm


def index(request):
    return render(request, "website/index.html")

def resume(request):
    return render(request, "website/resume.html")

def projects(request):
    return render(request, "website/projects.html")

def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, 'Thank you for subscribing! You will receive updates in your inbox.')
            return redirect('website:subscribe')  # Redirect back to the same page or another page
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
            return render(request, "website/subscribe.html", {'form': form})
    else:
        form = SubscriberForm()
        return render(request, "website/subscribe.html", {'form': form})

def blogHome(request):

    #Queries for all blog entries to give a listing on the blogHome page.
    BlogEntries = BlogEntry.objects.all().order_by('-blogDate')
    Context = {'BlogEntries': BlogEntries}

    return render(request, "website/bloghome.html", Context)
    

def blogPost(request, postID):

    entry = BlogEntry.objects.get(id=postID)
    other_entries = BlogEntry.objects.exclude(id=postID).order_by('-blogDate')[:10]
    
    return render(request, "website/blogentry.html", {
        'post': entry,
        'other_entries': other_entries
    })