from django.contrib import admin
from ads.models import Ad
from django.utils.html import format_html

class AdAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)
  list_display = ('title','image', 'description', 'created_at', 'creator')   
  

admin.site.register(Ad, AdAdmin)

from django.contrib import admin

# Register your models here.
