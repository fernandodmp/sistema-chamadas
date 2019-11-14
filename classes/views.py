from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from classes import models, forms
from users.models import Person
import random
import string
from django.contrib.auth.decorators import login_required
# Create your views here.
# TODO:
# [X] Visualização dos Cursos
# [X] Listagem de Curso na visão de todos
# [X] Criação de Aulas pelo dono do curso
# [X] Fechamento/Abertura de Aulas pelo dono do curso
# [] Registro de Presença de alunos
# [] Geração de relatório de presença do curso
# Seção Meus Cursos:
# [] Listagem de Curso dos quais o usuário é proprietário
# [] Listagem de Curso dos quais o usuário é participante
# [] Criação/Remoção de Cursos na visão do usuário logado


def list_courses(request):
    return render(request, 'classes/class_list.html', context={"courses": models.Course.objects.all()})


def course_page(request, id):
    is_owner = False

    course = models.Course.objects.get(pk=id)

    if(request.user == course.owner):
        is_owner = True

    lessons = course.lesson_set.all()

    ctx = {
        'course': course,
        'lessons': lessons,
        'is_owner': is_owner,
        'user': request.user
    }

    return render(request, 'classes/single_course.html', context=ctx)

def generate_auth_code():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])

@login_required
def add_lesson(request, course_id):
    course = get_object_or_404(models.Course, pk=course_id)
    if request.user == course.owner:
        code = generate_auth_code()
        new_lesson = models.Lesson(course=course, auth_code=code)
        new_lesson.save()
        return redirect('course', id=course_id)
    else:
        return render(request, 'errors/unauthorized.html', status=401)


@login_required
def close_lesson(request, id):
    lesson = get_object_or_404(models.Lesson, pk=id)
    if request.user == lesson.course.owner:
        lesson.on_going = False
        lesson.save()
        return redirect('course', id=lesson.course.id)
    else:
        return render(request, 'errors/unauthorized.html', status=401)


@login_required
def open_lesson(request, id):
    lesson = get_object_or_404(models.Lesson, pk=id)
    if request.user == lesson.course.owner:
        new_code = generate_auth_code()
        lesson.on_going = True
        lesson.auth_code = new_code
        lesson.save()
        return redirect('course', id=lesson.course.id)
    else:
        return render(request, 'errors/unauthorized.html', status=401)
