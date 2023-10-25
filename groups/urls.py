from django.urls import path

from .views import group_form, groups_list, group_edit

urlpatterns = [
    path("group/", group_form, name="group_form"),
    path("groups/", groups_list, name="groups_list"),
    path("group/<int:pk>", group_edit, name="group_edit"),
]
