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
HIDE_SIDEBAR = True
BOOTSTRAP_THEME = 'readable'
PYGMENTS_STYLE = 'murphy'
TWITTER_WIDGET_ID = True
TWITTER_USERNAME = 'tdhopper'
INDEX_SAVE_AS = None
PAGES_PATHS = ['pages']
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
IPYNB_USE_META_SUMMARY = True
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
AVATAR = 'static/headshot.jpg'
ABOUT_ME = ("I am a data scientist and software developer in cybersecurity. "
            "I enjoy math, computing, conversation, reading, hiking, photography, "
            "philosophy of science, and more.")
PROJECTS = [
    ("https://github.com/tdhopper/notes-on-dirichlet-processes/blob/master/README.md", "Notes on Dirichlet Processes"),
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
MENUITEMS = []
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

EXTERNAL_ME = [
    ["backpacking.png", "http://www.ultratall-ultralight.com/", "Ultralight Backpacking for the Ultratall", "Notes on gear.", ["read"]],
    ["dirichlet.png", "https://github.com/tdhopper/notes-on-dirichlet-processes",
        "Notes on Nonparametric Bayesian Methods and Dirichlet Processes", "", ["technical", "read"]],
    ["joehopper.png", "http://joseph-hopper.com/", "The Works of Joseph Hopper and Joe B. Hopper", "Archive of writings.", ["read"]],
    ["lda.png", "https://datamicroscopes.github.io/", "Bayesian nonparametric latent dirichlet allocation", "Python library.", ["technical"]],
    ["phd.png", "http://shouldigetaphd.com", "Should I Get a Ph.D.? ", "An Interview Series.", ["read"]],
    ["basketball.png", "http://doyouplayball.tumblr.com", "Do You Play Basketball?", "A journal.", ["read", "humor"]],
    ["profile_in_comp.png", "http://computationalimagination.com/interview_tim_hopper.php",
        "Profile in Computational Imagination", "Interview with me from 2015.", ["read", "interview"]],
    ["undersampled_radio.png", "https://undersampledrad.io/home/2016/10/intelligent-security",
        "Intelligent Security", "Interview with me from 2016.", ["listen", "interview"]],
    ["adversariall.png", "http://adversariallearning.com/episode-2-the-tallest-data-scientist.html",
        "The Tallest Data Scientist", "Interview with me from 2016.", ["listen", "interview"]],
    ["howiquit.png", "https://docs.google.com/presentation/d/1_wdSh2PFxiqBegt5PcatbEiQaganlgdb5bH7V2jHXZI/pub?start=false&loop=false&delayms=5000&slide=id.p",
        "How I Quit My Ph.D.", "Presentation from 2017.", ["read", "presentation"]],
    ["sharing.png", "https://www.youtube.com/watch?v=uRul8QdYvqQ", "Sharing Your Side Projects Online", "Presentation from 2016.", ["watch", "presentation"]],
    ["ecig.png", "http://www.jmir.org/2015/11/e251/", "Using Twitter Data to Gain Insights into E-cigarette Marketing", "Publication from 2015.", ["read", "technical"]],
    ["redis.png", "http://nbviewer.jupyter.org/github/tdhopper/Pickle-and-Redis/blob/master/Pickle%20and%20Redis.ipynb", "Pickle and Redis", "Presentation from 2012.", ["read", "technical", "presentation"]],
    ["pyspark.png", "http://nbviewer.jupyter.org/format/slides/github/tdhopper/rta-pyspark-presentation/blob/master/slides.ipynb#/", "Introduction to PySpark", "Presentation from 2015.", ["read", "technical", "presentation"]],
    ["orvideo.png", "https://www.youtube.com/watch?v=0gfBH4mC_iU", "Bringing Operations Research into the 21st Century with Online Video ", "Presentation from 2012.", ["watch", "presentation"]],
    ["olneyhymn.png", "http://olneyhymn.github.io", "Olney Hymn", "Collection of theology resources.", ["read"]],
    ["scikitlearn.png", "http://nbviewer.jupyter.org/format/slides/github/tdhopper/Research-Triangle-Analysts--Intro-to-scikit-learn/blob/master/Intro%20to%20Scikit-Learn.ipynb#/6", "Introduction to Scikit-Learn", "Presentation from 2013.", ["read", "technical", "presentation"]],
    ["simulation.png", "https://www.youtube.com/watch?v=Wy-XhT2sHgM", "Understanding Probabilistic Topic Models By Simulation",
        "Presentation from 2016.", ["watch", "presentation", "technical"]],
]
EXTERNAL_TAGS = set()
for project in EXTERNAL_ME:
    for tag in project[-1]:
        EXTERNAL_TAGS.add(tag.lower())
