from django.contrib import admin

# Register your models here.
from api.models import Movie, Rating

admin.site.register(Movie)
admin.site.register(Rating)
