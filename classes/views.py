from django.shortcuts import render
from .models import Course, Lesson
from users.models import Person

# Create your views here.
# TODO:
# [X] Visualização dos Cursos
# [X] Listagem de Curso na visão de todos
# [] Criação de Aulas pelo dono do curso
# [] Fechamento de Aulas pelo dono do curso
# [] Registro de Presença de alunos
# [] Geração de relatório de presença do curso
# Seção Meus Cursos:
# [] Listagem de Curso dos quais o usuário é proprietário
# [] Listagem de Curso dos quais o usuário é participante
# [] Criação/Remoção de Cursos na visão do usuário logado


def list_courses(request):
    return render(request, 'classes/class_list.html', context={"courses": Course.objects.all()})


def course_page(request, id):
    is_owner = False

    course = Course.objects.get(pk=id)
    if(request.user.is_authenticated and request.user == course.owner):
        is_owner = True
    lessons = course.lesson_set.all()
    return render(request, 'classes/single_course.html', context={'course': course, 'lessons': lessons, 'is_owner': is_owner, 'user': request.user})
