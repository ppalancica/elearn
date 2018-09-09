from django.db import models
from django.urls import reverse

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    author = models.CharField(max_length=255)
    # summary = models.CharField(max_length=255)
    # technology = models.CharField(max_length=100)
    # logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('courses:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.author

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.title
