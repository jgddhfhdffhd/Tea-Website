# core/admin.py

from django.contrib import admin
from .models import News, Like, Comment, Tea, TeaGarden, TeaHistory
from django import forms
from tinymce.widgets import TinyMCE

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'image')  # Show image in the list view
    search_fields = ('title', 'content')  # Add search functionality
    list_filter = ('created_at',)  # Filter by creation date

class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'news_article', 'created_at')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'news_article', 'created_at', 'content')

class TeaGardenAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description', 'image')
    search_fields = ('name', 'location')
    list_filter = ('location',)

class TeaHistoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'image')
    search_fields = ('title',)

class TeaAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image')
    search_fields = ('name',)




admin.site.register(Tea, TeaAdmin)
admin.site.register(TeaGarden, TeaGardenAdmin)
admin.site.register(TeaHistory, TeaHistoryAdmin)

admin.site.register(News, NewsAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Comment, CommentAdmin)