# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.inclusion_tag("aldryn_google_tag_manager/google_tag_manager.html")
def google_tag_manager(tag_id=''):
    if not tag_id and hasattr(settings, 'GOOGLE_TAG_MANAGER_ID'):
        tag_id = settings.GOOGLE_TAG_MANAGER_ID
    return {
        'tag_id': tag_id
    }

@register.simple_tag
def data_layer(**kwargs):
    data = []
    for key, value in kwargs.items():
        if value:
            data.append("'%s': '%s'" % (key.replace('_', '-'), value))
    return mark_safe('''<script>
    var dataLayer = window.dataLayer = window.dataLayer || [];
    dataLayer.push({
        %s
    });
  </script>''' % ', '.join(data))

@register.simple_tag
def to_list_if_exists(*args):
    return [arg for arg in args if arg]
