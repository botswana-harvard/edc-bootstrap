

class FilterMixin(object):

    allowed_filters = {}
    allowed_excludes = {}

    def get_queryset_filters(self):
        filters = {}
        for item in self.allowed_filters:
            if item in self.request.GET:
                filters[self.allowed_filters[item]] = self.request.GET[item]
        return filters

    def get_queryset_excludes(self):
        filters = {}
        for item in self.allowed_excludes:
            if item in self.request.GET:
                filters[self.allowed_filters[item]] = self.request.GET[item]
        return filters

    def get_queryset(self):
        if self.get_queryset_filters():
            return super(FilterMixin, self).get_queryset().filter(
                **self.get_queryset_filters()).exclude(**self.get_queryset_excludes())
        else:
            return super(FilterMixin, self).get_queryset()
