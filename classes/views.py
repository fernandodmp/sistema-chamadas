from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from classes import models, forms
from users.models import Person
import random
import string
from django.contrib.auth.decorators import login_required

def list_courses(request):
    return render(request, 'classes/class_list.html', context={"courses": models.Course.objects.all()})


def course_page(request, id):
    is_owner = False

    course = get_object_or_404(models.Course, pk=id)
    subscribe = forms.SubscribeForm()
    check_in = forms.CheckInForm()

    if(request.user == course.owner):
        is_owner = True

    lessons = course.lesson_set.all()

    ctx = {
        'subscribe': subscribe,
        'check_in': check_in,
        'course': course,
        'lessons': lessons,
        'is_owner': is_owner,
        'user': request.user
    }

    return render(request, 'classes/single_course.html', context=ctx)


def generate_auth_code():
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(6)])

@login_required
def subscribe_on_course(request, course_id):
    course = get_object_or_404(models.Course, pk=course_id)
    if request.user in course.participants.all():
        return render(request, 'errors/already_in.html', status=400)
    if request.method == "POST":
        form = forms.SubscribeForm(request.POST)
        if(form.is_valid()):
            key = form.cleaned_data['course_key']
            if key == course.access_key:
                course.participants.add(request.user)
                return redirect('course', id=course.id)
            else:
                return render(request, 'errors/wrong_key.html', status=400)

@login_required
def course_report(request, id):
    course = get_object_or_404(models.Course, pk=id)
    if request.user == course.owner:
        participants = course.participants.all()
        lessons = course.lesson_set.all()
        ctx = {'participants': participants, 'lessons': lessons, 'course':course}
        return render(request, 'classes/course_report.html', context = ctx)
    else:
        return render(request, 'errors/unauthorized.html', status=401)

@login_required
def new_course(request):
    if request.method == "POST":
        form = forms.CourseCreation(request.POST)
        if(form.is_valid()):
            course = form.save(commit=False)
            course.owner = request.user
            course.save()
            return redirect('course', id=course.id)
    else:
        form = forms.CourseCreation()
        return render(request, 'classes/create_course.html', context={'form':form})

@login_required
def my_courses(request):
    owned_courses = request.user.owner.all()
    subscribed_courses = request.user.participants.all()
    ctx = {"owned": owned_courses, "subscribed": subscribed_courses}
    return render(request, 'classes/my_courses.html', context=ctx)


@login_required
def delete_course(request, id):
    course = get_object_or_404(models.Course, pk=id)
    if request.user == course.owner:
        course.delete()
        return redirect('my_courses')
    else:
        return render(request, 'errors/unauthorized.html', status=401)

@login_required
def unsubscribe(request, id):
    course = get_object_or_404(models.Course, pk=id)
    course.participants.remove(request.user)
    return redirect('my_courses')


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

@login_required
def remove_lesson(request, id):
    lesson = get_object_or_404(models.Lesson, pk=id)
    if request.user == lesson.course.owner:
        lesson.delete()
        return redirect('course', id=lesson.course.id)
    else:
        return render(request, 'errors/unauthorized.html', status=401)

@login_required
def lesson_check_in(request, lesson_id):
    lesson = get_object_or_404(models.Lesson, pk=lesson_id)
    if request.user in lesson.attendants.all():
        return render(request, 'errors/already_in.html', status=400)
    if not lesson.on_going:
        return render(request, 'errors/closed_lesson.html', status=400)
    if request.method == "POST":
        form = forms.CheckInForm(request.POST)
        if(form.is_valid()):
            code = form.cleaned_data['auth_code']
            if code == lesson.auth_code:
                lesson.attendants.add(request.user)
                return redirect('course', id=lesson.course.id)
            else:
                return render(request, 'errors/wrong_key.html', status=400)