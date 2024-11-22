from django.db import models
from django.utils.timezone import now

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
        # Save the instance to ensure the file is uploaded
        super().save(*args, **kwargs)

        # Proceed only if a valid image is uploaded
        if self.blogPhoto and self.blogPhoto.name:
            from PIL import Image
            from io import BytesIO
            from django.core.files.base import ContentFile

            # Open the file directly from storage
            file_obj = self.blogPhoto.file
            img = Image.open(file_obj)

            # Check and resize the image if needed
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

                # Generate a valid filename if not present
                filename = self.blogPhoto.name or f"{self.pk}_resized.jpg"

                # Replace the original file with the resized version
                self.blogPhoto.delete(save=False)  # Delete the original file
                self.blogPhoto.save(filename, ContentFile(buffer.read()), save=False)

        # Save the instance again to update any changes
        super().save(*args, **kwargs)



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
