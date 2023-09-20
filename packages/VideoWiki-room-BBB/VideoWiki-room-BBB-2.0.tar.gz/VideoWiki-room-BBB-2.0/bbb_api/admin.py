from django.contrib import admin
from .models import Meeting, TemporaryFiles, NftDetails, ViewerDetails, MailTemplateDetails
# Register your models here.


@admin.register(Meeting)
class MeetAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name')

