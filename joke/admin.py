from django.contrib import admin
from joke.models import Article, Person

# Register your models here.
admin.site.register(Person)
admin.site.register(Article)