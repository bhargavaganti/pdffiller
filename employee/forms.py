from django import forms
from employee.models import Individual, Family


class FamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = "__all__"

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = "__all__"