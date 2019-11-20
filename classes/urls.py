from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_courses, name='all_courses'),
    path('my_courses', views.my_courses, name='my_courses'),
    path('new', views.new_course, name='create_course'),
    path('<int:id>', views.course_page, name='course'),
    path('<int:id>/delete', views.delete_course, name='delete_course'),
    path('<int:id>/unsubscribe', views.unsubscribe, name='unsubscribe'),
    path('<int:id>/report', views.course_report, name='course_report'),
    path('<int:course_id>/new_lesson', views.add_lesson, name='new_lesson'),
    path('<int:course_id>/subscribe',
         views.subscribe_on_course, name='subscribe_course'),
    path('lessons/<int:id>/close', views.close_lesson, name='close_lesson'),
    path('lessons/<int:id>/open', views.open_lesson, name='open_lesson'),
    path('lessons/<int:id>/remove', views.remove_lesson, name='remove_lesson'),
    path('lessons/<int:lesson_id>/check_in',
         views.lesson_check_in, name='check_in_lesson'),
]
