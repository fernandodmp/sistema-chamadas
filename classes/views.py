from django.shortcuts import render
from .models import Course, Lesson
from users.models import Person

# Create your views here.
# TODO:
# [] Criação/Remoção de Cursos na visão do usuário logado
# [] Visualização dos Cursos
# [X] Listagem de Curso na visão de todos
# [] Seção Meus Cursos
    # [] Listagem de Curso dos quais o usuário é proprietário
    # [] Listagem de Curso dos quais o usuário é participante
    # [] Criação/Remoção de Cursos na visão do usuário logado
# [] Criação de Aulas pelo dono do curso
# [] Fechamento de Aulas pelo dono do curso
# [] Registro de Presença de alunos
# [] Geração de relatório de presença do curso


def list_courses(request):
    return render(request, 'classes/class_list.html', context={"courses" : Course.objects.all()})