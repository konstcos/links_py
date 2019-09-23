from django.contrib import admin
from .models import Link

# admin.site.register(Link)
@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created')
    search_fields = ('name', 'url')
