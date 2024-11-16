from django.contrib import admin
from .models import BlogEntry, Subscriber
import csv
from django.http import HttpResponse


@admin.action(description="Export selected subscribers as CSV")
def export_subscribers_to_csv(modeladmin, request, queryset):
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


class SubscriberAdmin(admin.ModelAdmin):
    list_display = ("nameFirst", "nameLast", "subEmail", "dateSub")  # Adjust fields as needed
    actions = [export_subscribers_to_csv]  # Add the custom action here


# Register the models and admin classes
admin.site.register(BlogEntry)
admin.site.register(Subscriber, SubscriberAdmin)
