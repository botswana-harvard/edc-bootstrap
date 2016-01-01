import json
import socket

from datatableview.views import XEditableDatatableView
from django.http.response import HttpResponse
from django.utils import timezone


class EdcEditableDatatableView(XEditableDatatableView):

    modification_fields = ['user_modified', 'modified', 'hostname_modified']
    template_name = 'datatables_listview.html'

    def get_context_data(self, **kwargs):
        context = super(EdcEditableDatatableView, self).get_context_data(**kwargs)
        context['listview_title'] = self.model._meta.verbose_name_plural
        return context

    def update_object(self, form, obj):
        """ Saves the new value to the target object and adds in modification values. """
        field_name = form.cleaned_data['name']
        value = form.cleaned_data['value']
        setattr(obj, field_name, value)
        update_fields = self.update_modification_fields(obj)
        update_fields.append(field_name)
        save_kwargs = {}
        try:
            save_kwargs['update_fields'] = update_fields
            obj.save(**save_kwargs)
        except ValueError:
            save_kwargs['update_fields'] = [field_name]
            obj.save(**save_kwargs)
        data = json.dumps({
            'status': 'success',
        })
        return HttpResponse(data, content_type="application/json")

    def update_modification_fields(self, obj):
        """Returns a list of updated field names."""
        update_fields = []
        model_fields = [fld.name for fld in obj._meta.fields]
        for fld in self.modification_fields:
            if fld in model_fields:
                setattr(obj, fld, getattr(self, fld))
                update_fields.append(fld)
        return update_fields

    @property
    def user_modified(self):
        return self.request.user

    @property
    def modified(self):
        return timezone.now()

    @property
    def hostname_modified(self):
        return socket.gethostname()
