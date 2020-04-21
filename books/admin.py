from django.contrib import admin
from books.models import Author, Book, Tag
# Register your models here.

# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('name', 'birth_date')
admin.site.register(Author)

# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'num_pages', 'date_published', 'author', 'tags')

admin.site.register(Book)

# class TagAdmin(admin.ModelAdmin):
#     list_display = ('tag')

admin.site.register(Tag)

