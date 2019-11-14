from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courses, name='all_courses'),
    path('<int:id>', views.course_page, name='course'),
    path('<int:course_id>/new_lesson', views.add_lesson, name='new_lesson'),
    path('lessons/<int:id>/close', views.close_lesson, name='close_lesson'),
    path('lessons/<int:id>/open', views.open_lesson, name='open_lesson')
]
