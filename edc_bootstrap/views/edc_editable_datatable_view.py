import json

from datatableview.views import XEditableDatatableView
from django.http.response import HttpResponse


class EdcEditableDatatableView(XEditableDatatableView):

    model = None
    template_name = 'edc_bootstrap/datatables_listview.html'
    datatable_options = {
        'structure_template': "edc_bootstrap/bootstrap_structure.html",
    }

    def update_object(self, form, obj):
        """ Saves the new value to the target object. """
        field_name = form.cleaned_data['name']
        value = form.cleaned_data['value']
        setattr(obj, field_name, value)
        save_kwargs = {}
        save_kwargs['update_fields'] = [field_name]
        obj.save(**save_kwargs)
        data = json.dumps({
            'status': 'success',
        })
        return HttpResponse(data, content_type="application/json")
