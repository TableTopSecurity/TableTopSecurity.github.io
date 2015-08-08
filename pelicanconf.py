#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark Gondree, Zach Petersen'
SITENAME = u'TableTop Security'
SITEURL = 'https://localhost:8000'
SITELOGO = 'images/2497807.png'
SITELOGO_SIZE = '30px'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 6

TAG_CLOUD_MAX_ITEMS = 6

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Twitter Cards and Dependencies - Uses OpenGraph which is 
# set to true by default, if you have changed this Twitter Cards
# will not work. 
TWITTER_CARDS = True
TWITTER_USERNAME = 'TableTopSec'
TWITTER_WIDGET_ID ='620044429580066816'

PATH = 'content'

STATIC_PATHS = ['images', 'extras/css/tts.css']

EXTRA_PATH_METADATA = {
    'extras/css/tts.css': {'path': 'static/tts.css'}
    }
BANNER = 'images/go-2.jpg'
#TEMPLATE_PAGES = {'themes/pelican-bootstrap3/templates/home.html': 'pages/home.html'}

# Menu items
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DEFAULT_CTATEGORY = 'misc.'
INDEX_SAVE_AS = 'blog_index.html'
MENUITEMS = (('Blog', '/blog_index.html'),
			 ('About', '/pages/about.html'),)

DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_SERIES_ON_SIDEBAR = False

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/TableTopSec'),
          ('github', 'http://github.com/tabletopsecurity'),
          ('flickr', 'https://www.flickr.com/tabletopsecurity'),
          ('boardgamegeek', 'https://boardgamegeek.com/boardgamepublisher/23997/tabletop-security'))


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme related settings
THEME = 'themes/pelican-bootstrap3'
THEME_STATIC_PATHS=['static']
CSS_FILE='tts.css'
CUSTOM_CSS = 'static/tts.css'
USE_PAGER = True

# Caching
LOAD_CONTENT_CACHE = False