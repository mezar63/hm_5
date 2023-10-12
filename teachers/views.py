from django.shortcuts import render, redirect

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


def teachers_list(request):
    objects = Teacher.objects.all()
    return render(request, "get_teachers_list.html", {"objects": objects})