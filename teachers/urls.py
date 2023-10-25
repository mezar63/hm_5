from django.urls import path

from .views import teacher_form, teachers_list, teacher_edit, teacher_delete

urlpatterns = [
    path("teacher/", teacher_form, name="teacher_form"),
    path("teachers/", teachers_list, name="teachers_list"),
    path("teacher/<int:pk>", teacher_edit, name="teacher_edit"),
    path("teacher/delete/<int:pk>", teacher_delete, name="teacher_delete"),
]
