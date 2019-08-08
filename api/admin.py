from django.contrib import admin
from .models import Post,People
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'imgName', 'title','link']
    list_display_links = ['id', 'imgName']

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['id', 'imgName', 'name','subname','title']
    list_display_links = ['id', 'imgName','name']
