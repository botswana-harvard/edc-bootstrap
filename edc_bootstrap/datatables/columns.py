from datatableview.columns import BooleanColumn
from django.db import models


class MyBooleanColumn(BooleanColumn):
    model_field_class = models.BooleanField
    handles_field_classes = [models.BooleanField, models.NullBooleanField]
    lookup_types = ('exact', 'in')

    def prep_search_value(self, term, lookup_type):
        return None
