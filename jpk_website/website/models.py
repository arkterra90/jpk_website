from django.db import models
from django.utils.timezone import now

class BlogEntry(models.Model):
    blogDate = models.DateTimeField()
    blogAuthor = models.CharField(max_length=255)
    blogTitle = models.CharField(max_length=255)
    blogTag = models.CharField(max_length=255)
    blogText = models.TextField()
    blogPhoto = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.blogDate} {self.blogAuthor} {self.blogTitle} {self.blogTag} {self.blogText} {self.blogPhoto}"
    
class Subscriber(models.Model):
    nameFirst = models.CharField(max_length=100)
    nameLast = models.CharField(max_length=100)
    subEmail = models.EmailField()
    dateSub = models.DateField(default=now)

    def __str__(self):
        return f"{self.nameFirst} {self.nameLast} {self.subEmail} {self.dateSub}"