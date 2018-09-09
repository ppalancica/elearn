from django.db import models
from django.urls import reverse

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.last_name  + ' ' + self.first_name


class Course(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    summary = models.CharField(max_length=255, null=True, blank=True)
    # technology = models.CharField(max_length=100)
    # logo = models.CharField(max_length=1000)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('courses:course-detail', args=[str(self.slug)]) # kwargs={'pk': self.pk}

    def __str__(self):
        return self.title + ' ' + str(self.author)


class Module(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    course = models.ForeignKey(Course, related_name="modules", on_delete=models.CASCADE) # null=False, blank=False

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Lesson(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    module = models.ForeignKey(Module, related_name='lessons', on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title
