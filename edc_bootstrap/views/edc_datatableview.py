from datatableview.views import DatatableView


class EdcDatatableView(DatatableView):
    model = None
    template_name = 'edc_bootstrap/datatables_listview.html'

    def get_context_data(self, **kwargs):
        context = super(EdcDatatableView, self).get_context_data(**kwargs)
        context['model_name'] = self.model._meta.verbose_name
        return context
