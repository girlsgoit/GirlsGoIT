from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Track
from .models import Region
from .models import Member
from .models import Event
from .models import Story
from .models import MemberRole

admin.site.register(Track, MarkdownxModelAdmin)
admin.site.register(Region)
admin.site.register(Member)
admin.site.register(MemberRole)
admin.site.register(Event, MarkdownxModelAdmin)
admin.site.register(Story, MarkdownxModelAdmin)
