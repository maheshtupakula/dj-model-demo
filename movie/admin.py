from django.contrib import admin
from .models import Movie, Role, Actor, Salary
# Register your models here.



admin.site.register(Movie)
admin.site.register(Role)
admin.site.register(Actor)
admin.site.register(Salary)
