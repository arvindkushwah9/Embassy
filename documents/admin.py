from django.contrib import admin
from documents.models import Document
from django.utils.html import format_html

class DocumentAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)
  list_display = ('title', 'image','approved', 'created_at', 'creator', 'approved_url')   
  

admin.site.register(Document, DocumentAdmin)

