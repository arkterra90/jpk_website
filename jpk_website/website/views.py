from django.shortcuts import render, redirect
from django.contrib import messages
from .models import BlogEntry
from .forms import SubscriberForm
from django.http import JsonResponse
from django.template.loader import render_to_string


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
    BlogEntries = BlogEntry.objects.all().order_by('-blogDate')

    # Extract unique tags for dropdown
    unique_tags = set(
        tag.strip()
        for entry in BlogEntries
        for tag in entry.blogTag.split(",")
        if tag.strip()
    )

    # Filter based on selected tag
    selected_tag = request.GET.get('tag')
    if selected_tag:
        BlogEntries = BlogEntries.filter(blogTag__icontains=selected_tag)

    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        # For AJAX requests, return only the blog entries
        html = render_to_string("website/partials/blog_list.html", {"BlogEntries": BlogEntries})
        return JsonResponse({"html": html})

    # For normal requests, render the full page
    return render(request, "website/bloghome.html", {
        "BlogEntries": BlogEntries,
        "unique_tags": sorted(unique_tags),
    })
    

def blogPost(request, postID):

    entry = BlogEntry.objects.get(id=postID)
    other_entries = BlogEntry.objects.exclude(id=postID).order_by('-blogDate')[:10]
    
    return render(request, "website/blogentry.html", {
        'post': entry,
        'other_entries': other_entries
    })