#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alex Stephen'
SITENAME = u'Rambling Raptors'
SITEURL = u'http://www.ramblingraptors.com'
SITESUBTITLE = u'The ramblings of a college student'

TIMEZONE = u'America/Detroit'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME="/Users/Alex/Documents/Projects/Blog/crowsfoot"
PROFILE_IMAGE_URL = SITEURL + '/theme/img/logo.png'
