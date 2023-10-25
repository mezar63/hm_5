from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Teacher
from .forms import TeacherForm


def teacher_form(request):
    if request.method == "GET":
        form = TeacherForm()
        return render(request, "teacher_form.html", {"form": form})

    form = TeacherForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("teachers_list")

    return render(request, "teacher_form.html", {"form": form})


def teacher_edit(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == "GET":
        form = TeacherForm(instance=teacher)
        return render(request, "teacher_form.html", {"form": form})

    form = TeacherForm(request.POST, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect(reverse("teachers_list"))

    return render(request, "teacher_form.html", {"form": form})


def teacher_delete(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    try:
        teacher.delete()
    except IntegrityError as e:
        print(e)
    return redirect(reverse("teachers_list"))


def teachers_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers_list.html", {"teachers": teachers})
