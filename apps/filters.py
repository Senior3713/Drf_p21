from django.db.models import IntegerChoices
from django_filters import FilterSet, ChoiceFilter

from apps.models import Product


class ProductFilterSet(FilterSet):
    class Number(IntegerChoices):
        N1 = 1
        N2 = 2
        N3 = 3

    n = ChoiceFilter(choices=Number.choices)

    class Meta:
        model = Product
        fields = 'category',
