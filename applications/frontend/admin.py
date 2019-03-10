from django.contrib import admin

from .models import App, SearchQuery

admin.site.register(App)
admin.site.register(SearchQuery)
