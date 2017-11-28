from django.contrib import admin
# Register your models here.

from .models import Group, Artist, Member

admin.site.register(Group)
admin.site.register(Artist)
admin.site.register(Member)
