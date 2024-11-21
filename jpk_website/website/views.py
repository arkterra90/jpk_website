from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import BlogEntry
from .forms import SubscriberForm
from django.db.models import Q


# View for rendering the home page
def index(request):
    return render(request, "website/index.html")

# View for rendering the resume page
def resume(request):
    return render(request, "website/resume.html")

# View for rendering the projects page
def projects(request):
    return render(request, "website/projects.html")

# View for handling newsletter subscriptions
def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            form.save()
            messages.success(request, 'Thank you for subscribing! You will receive updates in your inbox.')
            return redirect('website:subscribe')  # Redirect to the subscription page
        else:
            # Handle invalid form submissions
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
            return render(request, "website/subscribe.html", {'form': form})
    else:
        # Display an empty subscription form for GET requests
        form = SubscriberForm()
        return render(request, "website/subscribe.html", {'form': form})

def blogHome(request):
    # Fetch all public blog entries, ordered by date (most recent first)
    BlogEntries = BlogEntry.objects.filter(blogPublic=True).order_by('-blogDate')

    # Extract unique tags for filtering from public blog entries
    unique_tags = set(
        tag.strip()
        for entry in BlogEntries
        for tag in entry.blogTag.split(",")
        if tag.strip()
    )

    # Apply tag-based filtering if a tag is selected
    selected_tag = request.GET.get('tag')
    if selected_tag:
        BlogEntries = BlogEntries.filter(blogTag__icontains=selected_tag)

    # Handle AJAX requests for dynamic content loading
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        html = render_to_string("website/partials/blog_list.html", {"BlogEntries": BlogEntries})
        return JsonResponse({"html": html})

    # Render the full blog home page for non-AJAX requests
    return render(request, "website/bloghome.html", {
        "BlogEntries": BlogEntries,
        "unique_tags": sorted(unique_tags),
    })

# View for displaying a single blog post
def blogPost(request, postID):
    # Fetch the public blog post by ID or return a 404 error if not found
    entry = get_object_or_404(BlogEntry, id=postID, blogPublic=True)

    # Fetch the 10 most recent public blog posts excluding the current one
    other_entries = BlogEntry.objects.filter(blogPublic=True).exclude(id=postID).order_by('-blogDate')[:10]

    return render(request, "website/blogentry.html", {
        'post': entry,
        'other_entries': other_entries,
    })


# Custom 404 error handler view
def custom_404(request, exception):
    return render(request, 'website/404.html', status=404)
