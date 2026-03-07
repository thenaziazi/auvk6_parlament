from django import forms

from apps.tasks.models import Tasks


class MinisterTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["event"].required = True
        self.fields["assigned_to"].required = True

    class Meta:
        model = Tasks
        fields = ["name", "description", "assigned_to", "deadline", "event"]