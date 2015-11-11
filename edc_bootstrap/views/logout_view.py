from django.views.generic.base import RedirectView
from django.contrib.auth import logout


class LogoutView(RedirectView):

    permanent = True

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)
