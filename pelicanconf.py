#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Tim Hopper'
SITENAME = u'tdhopper.com'
SITEURL = 'http://www.tdhopper.com'
TIMEZONE = 'America/New_York'

THEME = 'pelican-bootstrap3'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ["latex", 'i18n_subsites', 'ipynb.markup']
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
HIDE_SIDEBAR =  True
BOOTSTRAP_THEME = 'readable'
PYGMENTS_STYLE = 'murphy'
TWITTER_WIDGET_ID = True
TWITTER_USERNAME = 'tdhopper'
INDEX_SAVE_AS = None
PAGES_PATHS = ['pages']
IPYNB_USE_META_SUMMARY = True
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
AVATAR = 'static/headshot.jpg'
ABOUT_ME = ("I am a data scientist and software developer in cybersecurity. "
            "I enjoy math, computing, conversation, reading, hiking, photography, "
            "philosophy of science, and more.")
PROJECTS = [
    ("https://github.com/tdhopper/notes-on-dirichlet-processes/blob/master/README.md", "Notes on Dirichlet Processes"),
    ("http://til.tdhopper.com/", "Today I Learned"),
    ("http://shouldigetaphd.com/", "Should I Get a Phd?"),
    ("http://doyouplayball.tumblr.com/", "Do You Play Ball?"),
    ("http://www.ultratall-ultralight.com", "Ultralight Backpacking for the Ultratall"),
]
FAVORITES_TAG = 'featured'
OPEN_GRAPH_IMAGE = 'static/opengraphimage.jpg'
# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = "feeds/%s"
# CATEGORY_FEED_ATOM = "feeds/%s"
# TRANSLATION_FEED_ATOM = None
# TAG_FEED = "feeds/%s"

# Blogroll
# LINKS =
GOOGLE_ANALYTICS = 'UA-43428740-1'
USE_OPEN_GRAPH = True
MENUITEMS = [('Bio', '/about-me'),
             ('Archives', '/archives.html'),
             ]
BANNER = 'static/banner.jpg'
BANNER_SUBTITLE = 'Data Science. Python. Software Engineering. Math Jokes.'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_BREADCRUMBS = False
# Social widget
SOCIAL = (('Twitter', 'http://www.twitter.com/tdhopper'),
         ('Github', 'http://www.github.com/tdhopper'),
         ('Linkedin', 'http://www.linkedin.com/in/tdhopper'),
         ('Flickr', 'https://www.flickr.com/photos/tdhopper'),
         ('Instagram', 'https://www.instagram.com/tdhopper'),
         )
CUSTOM_CSS = 'static/custom.css'
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
