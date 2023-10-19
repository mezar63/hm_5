from django import forms

from .models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ["name", "teacher"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 255:
            raise forms.ValidationError("Name is too long")
        return name
