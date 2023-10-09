from django.shortcuts import render, redirect

from .models import Group
from .forms import GroupForm


def group_form(request):
    if request.method == "GET":
        form = GroupForm()
        return render(request, "group_form.html", {"form": form})

    form = GroupForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("groups_list")

    return render(request, "group_form.html", {"form": form})


def groups_list(request):
    objects = Group.objects.all()
    return render(request, "groups_list.html", {"objects": objects})