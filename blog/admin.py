from django.contrib import admin
from .models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    list_filter = ("tags", "date")
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)