from django.conf import settings


class EdcContextMixin(object):

    def get_context_data(self, **kwargs):
        context = super(EdcContextMixin, self).get_context_data(**kwargs)
        try:
            context['title'] = settings.PROJECT_TITLE
        except AttributeError:
            context['title'] = 'My Project'
        return context
