from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'),
    path('<slug:course_slug>/<slug:slug>/', views.LessonDetailView.as_view(), name='lesson-detail'), # <slug:course_slug>/lessons/<slug:slug>/
]
