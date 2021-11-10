from django.contrib import admin
from Product.models import Author, Book, Employees, Album, Songs


admin.site.register(Employees)
admin.site.register(Album)
admin.site.register(Songs)
admin.site.register(Author)
admin.site.register(Book)
