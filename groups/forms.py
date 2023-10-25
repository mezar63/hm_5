from django import forms

from .models import Group
from students.models import Student


class GroupForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance", None)
        super(GroupForm, self).__init__(*args, **kwargs)

        if instance:
            initial_data = [
                student.id
                for student in Group.objects.get(pk=instance.id).students.all()
            ]
            self.fields["students"].initial = initial_data

    class Meta:
        model = Group
        fields = ["name", "teacher"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 255:
            raise forms.ValidationError("Name is too long")
        return name
