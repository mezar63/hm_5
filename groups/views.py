from django.shortcuts import render, redirect

from .models import Group
from .forms import GroupForm


def group_form(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("groups_list")
    else:
        form = GroupForm()
    return render(request, "group_form.html", {"form": form})



def groups_list(request):
    groups = Group.objects.all()
    return render(request, "group_list.html", {"groups": groups})
