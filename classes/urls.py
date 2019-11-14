from django.urls import path
from .views import list_courses

urlpatterns = [
    path('', list_courses, name='all_courses'),
]
