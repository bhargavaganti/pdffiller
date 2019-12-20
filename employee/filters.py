import django_filters
from employee.models import Individual, Family

class FamilyFilter(django_filters.FilterSet):
    class Meta:
        model = Family
        fields = ['Fname', 'Fcontact', 'Faadhar', ]


class IndividualFilter(django_filters.FilterSet):
    class Meta:
        model = Individual
        fields = ['Fname', 'Fcontact', 'Faadhar', ]