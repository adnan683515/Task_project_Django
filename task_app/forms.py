from django import forms

from task_app.models import task


class task_form (forms.ModelForm):
    class Meta:
        model = task
        fields = '__all__'