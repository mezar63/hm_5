from django.shortcuts import render, redirect

from .models import Group
from .forms import GroupForm


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})

    form = GroupForm(request.POST)
    if form.is_valid():
        instance = form.save()
        for student in form.cleaned_data["students"]:
            instance.students.add(student)
        return redirect("groups_list")

    return render(request, "group_form.html", {"form": form})


def group_edit(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == "GET":
        form = GroupForm(instance=group)
        return render(request, "group_form.html", {"form": form})

    form = GroupForm(request.POST, instance=group)
    if form.is_valid():
        instance = form.save()
        for student in form.cleaned_data["students"]:
            instance.students.add(student)
        return redirect("groups_list")

    return render(request, "group_form.html", {"form": form})


def groups_list(request):
    objects = Group.objects.all()
    return render(request, "groups_list.html", {"objects": objects})