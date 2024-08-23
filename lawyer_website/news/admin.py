from django.contrib import admin
from .models import Article, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1  # Number of empty inline forms displayed


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at')
    search_fields = ('title', 'author__email')
    list_filter = ('published_at',)
    inlines = [CommentInline]  # Show comments inline with articles


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'article', 'created_at')
    search_fields = ('user__email', 'article__title')
    list_filter = ('created_at',)

