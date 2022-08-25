from django import forms

class EmployeeForm(forms.Form):
    file = forms.FileField()

    def __str__(self):
        return self.file