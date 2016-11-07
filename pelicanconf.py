#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Tim Hopper'
SITENAME = u'Stigler Diet'
SITEURL = 'http://stiglerdiet.com'
TIMEZONE = 'America/New_York'

THEME = 'pelican-svbhack'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["latex", 'ipynb']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'footnotes']
DEFAULT_LANG = u'en'
MARKUP = ('md', 'ipynb')
USER_LOGO_URL = SITEURL + '/uploads/logo.png'

PATH = 'content'
STATIC_PATHS = ['uploads']
ARTICLE_PATHS = ['articles']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGES_PATHS = ['pages']
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = "feeds/%s"
# CATEGORY_FEED_ATOM = "feeds/%s"
# TRANSLATION_FEED_ATOM = None
# TAG_FEED = "feeds/%s"

# Blogroll
# LINKS =

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/tdhopper'),
         ('Github', 'http://www.github.com/tdhopper'),
         ('Linkedin', 'http://www.linkedin.com/in/tdhopper'),
         ('Flickr', 'https://www.flickr.com/photos/tdhopper'),
         ('Instagram', 'https://www.instagram.com/tdhopper'),
         ('TIL', 'http://til.tdhopper.com/'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
