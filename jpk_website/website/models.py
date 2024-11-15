from django.db import models

class BlogEntry(models.Model):
    blogDate = models.DateTimeField()
    blogAuthor = models.CharField(max_length=255)
    blogTitle = models.CharField(max_length=255)
    blogTag = models.CharField(max_length=255)
    blogText = models.TextField()
    blogPhoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.blogDate} {self.blogAuthor} {self.blogTitle} {self.blogTag} {self.blogText} {self.blogPhoto}"