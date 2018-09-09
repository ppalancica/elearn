from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'),
]
