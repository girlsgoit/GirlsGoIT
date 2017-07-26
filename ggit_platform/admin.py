from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Track


admin.site.register(Track, MarkdownxModelAdmin)