from django.contrib import admin
from notifications.models import Notification
from django.utils.html import format_html

class NotificationAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)
  list_display = ('title', 'created_at', 'creator', 'receiver')   
  

admin.site.register(Notification, NotificationAdmin)

