from django.contrib import admin

from .models import Event
admin.site.register(Event)



from markdownx.admin import MarkdownxModelAdmin
from .models import Track
from .models import Region
from .models import Member
from .models import Story


# Register your models here.
admin.site.register(Track, MarkdownxModelAdmin)
admin.site.register(Member)
admin.site.register(Region)
admin.site.register(Story)
