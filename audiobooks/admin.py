from django.contrib import admin
from .models import Audiobooks, Narrator, Publisher, Author

admin.site.register(Audiobooks)
admin.site.register(Narrator)
admin.site.register(Publisher)
admin.site.register(Author)