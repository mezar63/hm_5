from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "year", "groups"]
        widgets = {
            "groups": forms.CheckboxSelectMultiple,
        }

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) > 50:
            raise forms.ValidationError("Max year size is 50 letters")
        return first_name

    def clean_year(self):
        year = self.cleaned_data["year"]
        if len(year) > 4:
            raise forms.ValidationError("Max year size is 4 letters")
        return year
