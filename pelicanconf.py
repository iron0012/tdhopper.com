#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Tim Hopper'
SITENAME = u'stiglerdiet.com'
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
STATIC_PATHS = ['uploads', 'static']
ARTICLE_PATHS = ['articles']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DISPLAY_RECENT_POSTS_ON_SIDEBAR =  True
BOOTSTRAP_THEME = 'readable'
TWITTER_WIDGET_ID = True
TWITTER_USERNAME = 'tdhopper'
PAGES_PATHS = ['pages']
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
AVATAR = 'uploads/logo.png'
ABOUT_ME = ("I am a data scientist and software developer in cybersecurity. "
            "I enjoy math, computing, conversation, reading, hiking, photography, "
            "philosophy of science, and the history of religion in America.")

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = "feeds/%s"
# CATEGORY_FEED_ATOM = "feeds/%s"
# TRANSLATION_FEED_ATOM = None
# TAG_FEED = "feeds/%s"

# Blogroll
# LINKS =
MENUITEMS = [('About Me', '/about-me'),
             ('Today I Learned', 'http://til.tdhopper.com/'),
             ('Archives', '/archives.html')]
BANNER = 'static/banner.jpg'
BANNER_SUBTITLE = 'Data Science. Python. Software Engineering. Math Jokes.'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = True
# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/tdhopper'),
         ('Github', 'http://www.github.com/tdhopper'),
         ('Linkedin', 'http://www.linkedin.com/in/tdhopper'),
         ('Flickr', 'https://www.flickr.com/photos/tdhopper'),
         ('Instagram', 'https://www.instagram.com/tdhopper'),
         )
CUSTOM_CSS = 'static/custom.css'
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
