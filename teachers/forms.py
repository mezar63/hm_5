from django import forms

from .models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ["name", "birth_date", "subjects"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 255:
            raise forms.ValidationError("Name is too long")
        return name
