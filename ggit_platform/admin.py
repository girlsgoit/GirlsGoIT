from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Track
from .models import Region
from .models import Member


# Register your models here.
admin.site.register(Track, MarkdownxModelAdmin)
admin.site.register(Member)
admin.site.register(Region)

