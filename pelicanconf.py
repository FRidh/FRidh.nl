#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Frederik Rietdijk'
SITENAME = u'FRidh\'s blog'
#SITEURL = 'http://fridh.nl'
SITESUBTITLE = "Discovery consists of seeing what everybody has seen and thinking what nobody has thought -- Albert Szent-Gyorgyi"

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'category/%s.atom.xml'
TAG_FEED_ATOM = 'tag/%s.atom.xml'


## Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
          #('Python.org', 'http://python.org/'),
          #('Jinja2', 'http://jinja.pocoo.org/'),
          #('You can modify those links in your config file', '#'),)

## Social widget
#SOCIAL = (("github", "http://github.com/FRidh"),
          #("lastfm", "http://last.fm/user/FRidh")

PATH = "content"

PAGE_PATHS = ["pages"]
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

ARTICLE_URL = "{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"


OUTPUT_PATH = "output"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/pelican-octopress-theme"
#THEME = "pelican-themes/fresh"
#THEME = "/home/freddy/blog/pelican-themes/tuxlite_tbs"

DEFAULT_CATEGORY = "Blog"

#TYPOGRIFY = True

SEARCH_BOX = True

GITHUB_URL = "http://github.com/FRidh"
GITHUB_USER = "FRidh"

SUMMARY_MAX_LENGTH = 50

DEFAULT_PAGINATION = False

PLUGIN_PATHS = ['/home/freddy/Code/pelican-plugins/']
#PLUGINS = ['liquid_tags.youtube', 'liquid_tags.notebook']

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
