from django.urls import path

from .views import student_form, student_list, student_edit, student_delete

urlpatterns = [
    path("student/", student_form, name="student_form"),
    path("students/", student_list, name="student_list"),
    path("student/<int:pk>", student_edit, name="student_edit"),
    path("student/delete/<int:pk>", student_delete, name="student_delete"),
]
