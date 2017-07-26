from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Track
from .models import Region
from .models import Member
from .models import Event
from .models import Story

admin.site.register(Track, MarkdownxModelAdmin)
admin.site.register(Member)
admin.site.register(Region)
admin.site.register(Event)
admin.site.register(Story)
