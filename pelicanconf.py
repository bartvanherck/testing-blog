#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bart Vanherck'
SITENAME = u'Software And Testing'
SITEURL = 'http://bartvanherck.github.io'
FIXEDSITEURL = 'http://bartvanherck.github.io'
#SITEURL = 'http://localhost:8000'
#SITEURL = 

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DISQUS_SITENAME = "swandtesting"
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
SOCIAL = (('Twitter', 'https://twitter.com/vherckb'),)

DEFAULT_PAGINATION = 9

TWITTER_USERNAME = "vherckb"
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME = "themes/bavh-pelican"

RECENT_POST_COUNT = 9
# SITELOGO = "Vanamo_Logo.png"
HIDE_SITENAME = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
ABOUT_ME = '<div>Bart Vanherck</div><div>software tester</div>'
