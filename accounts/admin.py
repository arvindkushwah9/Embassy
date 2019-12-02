from django.contrib import admin
from accounts.models import UserProfile
from django.utils.html import format_html

class UserProfileAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)
  list_display = ('user','passport_number', 'phone_number')   
  

admin.site.register(UserProfile, UserProfileAdmin)

