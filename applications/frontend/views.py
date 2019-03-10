import re

from django.template.defaultfilters import register
from django.views import generic
from app_store.utils import helpers
from applications.frontend.models import App


@register.filter
def get_string_as_list(value):
    """Evaluate a string if it contains []"""
    if '[' and ']' in value:
        return eval(value)


@register.filter
def bytestring(value):
    """Convert bytestring"""
    from django import template
    s = value
    t = template.Template('{{ s }}')
    return t.render(template.Context({'s': s}))


class AppHome(generic.ListView):
    """
    View for App Store AppHome
    """
    template_name = 'frontend/home.html'
    context_object_name = 'apps'

    def get_queryset(self):
        queryset = App.objects.all().order_by('?')
        if queryset:
            return queryset
        else:
            return []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class AppSearch(generic.ListView):
    """
    View for Search App
    """
    template_name = 'frontend/home.html'
    context_object_name = 'apps'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            query = re.sub('\s+', ' ', query).strip()
            return helpers.get_search_data(query)
        else:
            return []

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['title'] = 'Search for " {} "'.format(re.sub('\s+', ' ', query).strip())
        return context


class AppDetails(generic.DetailView):
    """
    View for App Details
    """
    template_name = 'frontend/details.html'
    slug_field = "app_id"
    slug_url_kwarg = "app_id"
    context_object_name = 'details'

    def get_queryset(self):
        # update app details if not scrapped
        helpers.get_details(self.kwargs.get('app_id'))
        return App.objects.filter(app_id=self.kwargs.get('app_id'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_queryset().values_list('title', flat=True).first()
        return context
