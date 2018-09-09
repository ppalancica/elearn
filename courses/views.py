from django.views import generic
from .models import Course, Module
# from django.contrib.auth.mixins import LoginRequiredMixin
# https://docs.djangoproject.com/en/2.1/topics/auth/default/#the-loginrequired-mixin

# Create your views here.

class IndexView(generic.ListView):
    # login_url = 'login'
    # redirect_field_name = 'redirect_to'

    template_name = 'courses/index.html'

    # the default is object_list, but we want to use all_courses inside the views.py file
    # context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.all()

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'courses/detail.html'
