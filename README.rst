Aldryn Google Tag Manager
=========================

A simple Google Tag Manager template tag for your CMS projects.

{% load google_tag_manager_tags %}
{% google_tag_manager YOUR_TAG_ID %}

Or, if you've already set GOOGLE_TAG_MANAGER_ID in your settings, you can just
use: ::

{% google_tag_manager %}
