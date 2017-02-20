#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Tim Hopper'
SITENAME = u'Tim Hopper: stiglerdiet.com'
SITEURL = 'http://stiglerdiet.com'
TIMEZONE = 'America/New_York'

THEME = 'pelican-bootstrap3'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["latex", 'i18n_subsites']
EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'footnotes']
JINJA_EXTENSIONS = ['jinja2.ext.i18n']
DEFAULT_LANG = u'en'
MARKUP = ('md', )
USER_LOGO_URL = SITEURL + '/uploads/logo.png'

PATH = 'content'
STATIC_PATHS = ['uploads']
ARTICLE_PATHS = ['articles']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DISPLAY_RECENT_POSTS_ON_SIDEBAR =  True
TWITTER_WIDGET_ID = True
TWITTER_USERNAME = 'tdhopper'
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
MENUITEMS = [('About Me', '/about-me')]
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = True
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
