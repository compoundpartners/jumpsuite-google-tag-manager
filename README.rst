Aldryn Google Tag Manager
=========================

Aldryn Google Tag Manager provides an easy-to-use `Google Tag Manager <http://www.google.com/tagmanager/>`_ template 
tag for your `Aldryn <http://aldryn.com>`_ and `django CMS <http://django-cms>`_ projects.

A tag is snippet of JavaScript that sends information to a third party, such as Google. If you don't use a tag
management solution such as Google Tag Manager, you need to add these snippets of JavaScript directly to the source
code of your site. In contrast, with Google Tag Manager, you no longer need to maintain each of these JavaScript
snippets in your source code; instead, you specify the tags that you want to fire, and when you want them to fire, in
the Google Tag Manager user interface.

Aldryn Google Tag Manager makes this available for your django CMS project - provide the Google Tag Manager ID for
this site, and it will do the rest::

    {% load google_tag_manager_tags %}
    {% google_tag_manager YOUR_TAG_ID %}

Or, if you've already set GOOGLE_TAG_MANAGER_ID in your settings, you can just
use: ::

    {% google_tag_manager %}
