from datatableview.views import DatatableView


class EdcDatatableView(DatatableView):

    template_name = 'datatables_listview.html'

    def get_context_data(self, **kwargs):
        context = super(EdcDatatableView, self).get_context_data(**kwargs)
        context['listview_title'] = self.model._meta.verbose_name_plural
        return context
