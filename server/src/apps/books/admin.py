from django.contrib import admin
from .models import Books, BookCover, Genre, BookState, Rating

# admin.site.register(BookState)
admin.site.register(Rating)

class TabularInlineImage(admin.TabularInline):
    model = BookCover
    extra = 0
    fields = ['book']

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    
@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    inlines = [TabularInlineImage, ]
    list_display = ('slug','user', 'title', 'created_at')
    list_display_links = ('user',)
    list_filter = ('genre', 'created_at')
    search_fields = ('user', 'genre__name')
