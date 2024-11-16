from django.test import TestCase
from django.urls import reverse
from .models import Subscriber, BlogEntry


class ViewTests(TestCase):
    def setUp(self):
        # Set up any required data
        Subscriber.objects.create(nameFirst="John", nameLast="Doe", subEmail="john.doe@example.com")
        BlogEntry.objects.create(
            blogTitle="Test Blog",
            blogText="This is a test blog.",
            blogAuthor="Author Name",
            blogDate="2024-11-01"
        )

    def test_index_view(self):
        """Test the index view for a successful response."""
        response = self.client.get(reverse("website:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "website/index.html")

    def test_blog_home_view(self):
        """Test the blog home view for a successful response."""
        response = self.client.get(reverse("website:blogHome"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "website/bloghome.html")

    def test_subscribe_view(self):
        """Test the subscribe view for a successful response and form submission."""
        response = self.client.get(reverse("website:subscribe"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "website/subscribe.html")

        # Test form submission
        response = self.client.post(
            reverse("website:subscribe"),
            {"nameFirst": "Jane", "nameLast": "Doe", "subEmail": "jane.doe@example.com"}
        )
        self.assertEqual(response.status_code, 302)  # Assuming a redirect on successful form submission
        self.assertTrue(Subscriber.objects.filter(subEmail="jane.doe@example.com").exists())

    def test_blog_post_view(self):
        """Test a single blog post view."""
        blog = BlogEntry.objects.first()
        response = self.client.get(reverse("website:blogPost", kwargs={"postID": blog.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "website/blogentry.html")

    def test_non_existent_view(self):
        """Test that a non-existent URL returns a 404."""
        response = self.client.get("/non-existent-url/")
        self.assertEqual(response.status_code, 404)
