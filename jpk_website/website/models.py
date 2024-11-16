from django.db import models
from django.utils.timezone import now

# Model representing a blog entry
class BlogEntry(models.Model):
    blogDate = models.DateTimeField()  # Date and time of the blog post
    blogAuthor = models.CharField(max_length=255)  # Name of the blog author
    blogTitle = models.CharField(max_length=255)  # Title of the blog post
    blogTag = models.CharField(max_length=255)  # Comma-separated tags for the blog post
    blogText = models.TextField()  # Main content of the blog post
    blogPhoto = models.ImageField(
        upload_to='blog_photos/', null=True, blank=True
    )  # Optional photo associated with the blog post

    def __str__(self):
        """
        String representation of the BlogEntry model.
        Shows a brief summary including the date, author, title, and tags.
        """
        return f"{self.blogDate} {self.blogAuthor} {self.blogTitle} {self.blogTag}"

# Model representing a subscriber to the blog or newsletter
class Subscriber(models.Model):
    nameFirst = models.CharField(max_length=100)  # Subscriber's first name
    nameLast = models.CharField(max_length=100)  # Subscriber's last name
    subEmail = models.EmailField()  # Subscriber's email address
    dateSub = models.DateField(default=now)  # Date the subscriber signed up

    def __str__(self):
        """
        String representation of the Subscriber model.
        Displays the subscriber's full name and email.
        """
        return f"{self.nameFirst} {self.nameLast} ({self.subEmail})"
