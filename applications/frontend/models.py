from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel


class App(TimeStampedModel):
    app_id = models.CharField(_('App ID'), max_length=255, null=True, blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    description_html = models.TextField(_('HTML Description'), null=True, blank=True)
    developer_id = models.CharField(_('Developer ID'), max_length=50, null=True, blank=True)
    developer = models.CharField(_('Developer'), max_length=255, null=True, blank=True)
    developer_address = models.TextField(_('Developer Address'), null=True, blank=True)
    developer_email = models.EmailField(_('Developer Email'), null=True, blank=True)
    developer_url = models.URLField(_('Developer URL'), null=True, blank=True)
    free = models.BooleanField(_('Is Free'), default=False)
    full_price = models.CharField(_('Full Price'), max_length=50, null=True, blank=True)
    icon = models.URLField(_('Icon'), null=True, blank=True)
    price = models.CharField(_('Price'), max_length=50, null=True, blank=True)
    score = models.CharField(_('Rating'), max_length=100, null=True, blank=True)
    title = models.CharField(_('Title'), max_length=255, null=True, blank=True)
    url = models.URLField(_('URL'), null=True, blank=True)
    category = models.CharField(_('Category'), max_length=255, null=True, blank=True)
    content_rating = models.CharField(_('Content Rating'), max_length=255, null=True, blank=True)
    current_version = models.CharField(_('Current Version'), max_length=100, null=True, blank=True)
    editors_choice = models.BooleanField(_('Editors Choice'), default=False)
    installs = models.CharField(_('Installs'), max_length=50, null=True, blank=True)
    recent_changes = models.TextField(_('Recent Changes'), null=True, blank=True)
    required_android_version = models.CharField(_('Android Version'), max_length=100, null=True, blank=True)
    reviews = models.CharField(_('Reviews'), max_length=50, null=True, blank=True)
    screenshots = models.TextField(_('Screenshots'), null=True, blank=True)
    size = models.CharField(_('Size'), max_length=50, null=True, blank=True)
    updated = models.DateField(_('Updated'), null=True, blank=True)
    video = models.TextField(_('Video'), null=True, blank=True)

    class Meta:
        verbose_name = _('App')
        verbose_name_plural = _('Apps')

    def __str__(self):
        return self.app_id


class SearchQuery(TimeStampedModel):
    query = models.TextField(_('Search Query'), null=True, blank=True, unique=True)

    class Meta:
        verbose_name = _('Search Query')
        verbose_name_plural = _('Search Queries')

    def __str__(self):
        return self.query
