#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bart Vanherck'
SITENAME = u'Software And Testing'
SITEURL = 'http://bartvanherck.github.io'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_ALL_RSS = 'feeds/blog.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 6

TWITTER_USERNAME = "vherckb"
# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "themes/bavh"
