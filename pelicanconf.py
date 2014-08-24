#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tim Hopper'
SITENAME = u'Stigler Diet'
SITEURL = 'http://stiglerdiet.com'
TIMEZONE = 'America/New_York'

THEME = 'themes/pelican-svbhack'
PLUGIN_PATH = "plugins"
PLUGINS = ["latex", 'pelican_gist']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'footnotes']
DEFAULT_LANG = u'en'


STATIC_PATHS = ['uploads']
PAGE_DIR = 'pages'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_DIR = 'articles'
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
TAG_FEED = "feeds/%s"
TAG_FEED_RSS = "feeds/%s"

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/tdhopper'),
         ('Github', 'http://www.github.com/tdhopper'),
         ('Linkedin', 'http://www.linkedin.com/in/tdhopper'),
         ('Google+', 'https://plus.google.com/u/0/118317721686581801159/posts'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
