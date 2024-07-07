from django import forms

from cetagory_app.models import Task_cetagory

class Cetagory_form (forms.ModelForm):
    class Meta:
        model = Task_cetagory
        fields = "__all__"