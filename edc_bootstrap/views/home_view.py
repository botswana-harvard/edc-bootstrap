from django.views.generic.base import TemplateView

from .edc_context_mixin import EdcContextMixin
from braces.views import LoginRequiredMixin


class HomeView(LoginRequiredMixin, EdcContextMixin, TemplateView):
    template_name = 'home.html'
