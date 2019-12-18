from django.contrib import admin

from .models import Article, Comment
from weather.models import City

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(City)
