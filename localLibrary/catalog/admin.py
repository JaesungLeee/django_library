from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language
# Register your models here.

#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(BookInstance)

admin.site.register(Genre)
admin.site.register(Language)

# Define the admin class
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    class BooksInline(admin.TabularInline):
        model = Book

    list_display = ('last_name', 'first_name')
    # fields = ['first_name', 'last_name']
    inlines = [BooksInline]
    pass

# Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    class BooksInstanceInline(admin.TabularInline):
        model = BookInstance

    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    pass