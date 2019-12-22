from django import forms

from employee.models import Individual, Family
import pdb

class FamilyForm(forms.ModelForm):
    my_object = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,)
    class Meta:
        model = Family
        fields = "__all__"
    def is_valid(self):
        # run the parent validation first
        valid = super(FamilyForm, self).is_valid()
        # we're done now if not valid
        if not valid:
            return True
        return False

class FamilyForm1(forms.ModelForm):

    class Meta:
        model = Family
        fields = "__all__"


class IndividualForm(forms.ModelForm):
    my_object = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,)

    class Meta:
        model = Individual
        fields = "__all__"

    def is_valid(self):
        # run the parent validation first
        valid = super(IndividualForm, self).is_valid()
        # we're done now if not valid
        if not valid:
            return True
        return False

class IndividualForm1(forms.ModelForm):

    class Meta:
        model = Individual
        fields = "__all__"

class SearchForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
    contact = forms.CharField(max_length=14,required=False)
    aadhar = forms.CharField(max_length=20,required=False)
