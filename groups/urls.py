from django.urls import path

from .views import group_form, groups_list

urlpatterns = [
    path("group/", group_form, name="group_form"),
    path("groups/", groups_list, name="groups_list"),
]
