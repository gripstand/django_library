from django.contrib import admin
from .models import Author,Book,Language,BookInstance,Genre

# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Language)
admin.site.register(BookInstance)
admin.site.register(Genre)