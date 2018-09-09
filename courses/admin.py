from django.contrib import admin
from .models import Author, Course, Module, Lesson

# Register your models here.

admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
