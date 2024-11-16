from django.contrib import admin
from .models import BlogEntry, Subscriber
from .forms import EmailForm
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mass_mail
from django.urls import path
from django.shortcuts import render
from django.contrib import messages

# Action: Export selected subscribers as a CSV file
@admin.action(description="Export selected subscribers as CSV")
def export_subscribers_to_csv(modeladmin, request, queryset):
    """
    Creates a downloadable CSV file containing details of the selected subscribers.
    """
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="subscribers.csv"'

    # Create the CSV writer.
    writer = csv.writer(response)

    # Write the header row.
    writer.writerow(["First Name", "Last Name", "Email", "Date Subscribed"])

    # Write the data rows.
    for subscriber in queryset:
        writer.writerow([subscriber.nameFirst, subscriber.nameLast, subscriber.subEmail, subscriber.dateSub])

    return response

# Action: Send mass email to selected subscribers
@admin.action(description="Send mass email to selected subscribers")
def send_email_to_subscribers(modeladmin, request, queryset):
    """
    Renders a form in the admin panel to compose and send mass emails to the selected subscribers.
    """
    if "apply" in request.POST:
        # Handle the form submission
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            recipients = queryset.values_list("subEmail", flat=True)

            # Prepare messages for send_mass_mail
            emails = [(subject, message, 'your-email@example.com', [email]) for email in recipients]

            # Send emails using send_mass_mail
            sent_count = send_mass_mail(emails, fail_silently=False)

            messages.success(request, f"Email sent to {sent_count} subscribers.")
            return HttpResponseRedirect(request.get_full_path())

    else:
        form = EmailForm()

    # Render a page with the form
    return render(
        request,
        "admin/send_email.html",
        {"form": form, "subscribers": queryset},
    )

# Admin class for managing Subscriber objects in the admin panel
class SubscriberAdmin(admin.ModelAdmin):
    """
    Customizes the admin interface for the Subscriber model, including list display,
    admin actions, and a custom URL for sending emails.
    """
    # Fields to display in the admin list view
    list_display = ("nameFirst", "nameLast", "subEmail", "dateSub")

    # Actions available in the admin interface
    actions = [export_subscribers_to_csv, send_email_to_subscribers]

    def get_urls(self):
        """
        Adds a custom URL to the admin interface for sending emails.
        """
        urls = super().get_urls()
        custom_urls = [
            path(
                "send_email/",
                self.admin_site.admin_view(send_email_to_subscribers),
                name="send_email_to_subscribers",
            ),
        ]
        return custom_urls + urls

# Register the BlogEntry model in the admin panel
admin.site.register(BlogEntry)

# Register the Subscriber model with the custom SubscriberAdmin class
admin.site.register(Subscriber, SubscriberAdmin)
