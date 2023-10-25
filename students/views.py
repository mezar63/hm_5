from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import StudentForm
from .models import Student


def student_form(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "student_form.html", {"form": form})

    form = StudentForm(request.POST)
    if form.is_valid():
        instance = form.save()
        for group in form.cleaned_data["groups"]:
            instance.groups.add(group)

    return redirect(reverse("student_list"))


def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "GET":
        form = StudentForm(instance=student)
        return render(request, "student_form.html", {"form": form})

    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
        instance = form.save()
        instance.groups.clear()

        for group in form.cleaned_data["groups"]:
            instance.groups.add(group)

        return redirect(reverse("student_list"))

    return render(request, "student_form.html", {"form": form})


def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect(reverse("student_list"))


def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})
