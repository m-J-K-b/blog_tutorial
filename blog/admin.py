from django.contrib import admin

from .models import Post, Category, Comment

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'intro', 'body', 'date_added']
    list_display = ['title', 'slug', 'category', 'date_added', 'status']
    list_filter = ['category', 'date_added', 'status']
    inlines = (CommentItemInline, )
    prepopulated_fields = {'slug': ('title', )}

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title', )}

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name, date_added, post']
    list_display = ['name', 'post', 'date_added']
    list_filter = ['name', 'post', 'date_added']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)

