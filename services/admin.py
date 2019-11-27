from django.contrib import admin
from services.models import Service
from django.utils.html import format_html

class ServiceAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)
  list_display = ('title','image', 'description', 'created_at', 'creator')   
  

admin.site.register(Service, ServiceAdmin)

from django.contrib import admin

# Register your models here.
