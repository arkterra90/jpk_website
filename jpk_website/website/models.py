from django.db import models
from django.utils.timezone import now
from PIL import Image


from ckeditor.fields import RichTextField

class BlogEntry(models.Model):
    blogDate = models.DateTimeField()  # Date and time of the blog post
    blogAuthor = models.CharField(max_length=255)  # Name of the blog author
    blogTitle = models.CharField(max_length=255)  # Title of the blog post
    blogTag = models.CharField(max_length=255)  # Comma-separated tags for the blog post
    blogText = RichTextField()  # Main content of the blog post with CKEditor
    blogPhoto = models.ImageField(
        upload_to='blog_photos/', null=True, blank=True
    )  # Updated: saves to "media/blog_photos/"
    blogPublic = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Call the parent class's save method first to handle initial saving
        super().save(*args, **kwargs)

        # Check if there's a photo and process it
        if self.blogPhoto:
            from PIL import Image
            from io import BytesIO
            from django.core.files.base import ContentFile

            # Open the uploaded image
            img = Image.open(self.blogPhoto)

            # Check if the image height exceeds 1080px
            if img.height > 1080:
                # Calculate the new width while maintaining aspect ratio
                aspect_ratio = img.width / img.height
                new_height = 1080
                new_width = int(new_height * aspect_ratio)

                # Resize the image
                img = img.resize((new_width, new_height), Image.LANCZOS)

                # Save the resized image to a BytesIO buffer
                buffer = BytesIO()
                img.save(buffer, format='JPEG')
                buffer.seek(0)

                # Save the resized image back to the `blogPhoto` field
                self.blogPhoto.save(self.blogPhoto.name, ContentFile(buffer.read()), save=False)


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
