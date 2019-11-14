from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courses, name='all_courses'),
    path('<int:id>', views.course_page, name='course'),
]
