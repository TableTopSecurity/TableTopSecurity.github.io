#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark Gondree, Zachary NJ Peterson'
SITENAME = u'TableTop Security'
SITEURL = 'http://localhost:8000'
SITELOGO = 'images/2497807.png'
SITELOGO_SIZE = '30px'
FAVICON = 'images/favicon.ico'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = 5
USE_PAGER = False

# Home / index.html
NEWS_ITEMS = 5

# Plugins
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['tag_cloud']

# Tag Cloud options
TAG_CLOUD_MAX_ITEMS = 200
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 3
TAGS_URL = 'tags.html'

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

STATIC_PATHS = ['images', 'extras/css/tts.css', 'extras/CNAME']

EXTRA_PATH_METADATA = {
    'extras/css/tts.css': {'path': 'static/tts.css'},
    'extras/CNAME' : {'path': 'CNAME'},
}

# Banner options
BANNER = 'images/go-2.jpg'
BANNER_ALL_PAGES = True  # well, not really, lets restrict it
BANNER_PAGES = ['index.html']
MOVE_MENU_TO_TOP = True

# Category options
USE_FOLDER_AS_CATEGORY = True
CATEGORY_SAVE_AS = '{slug}.html'
DEFAULT_CATEGORY = 'Blog'

# Article saving options
ARTICLE_URL = 'article/{slug}.html'
ARTICLE_SAVE_AS = 'article/{slug}.html'
INDEX_SAVE_AS = 'all.html'
DISPLAY_ARTICLE_INFO_ON_INDEX = True
SUMMARY_MAX_LENGTH = 100

# Article meta info shown
SHOW_ARTICLE_AUTHOR = True
ARTICLE_AUTHORS_PAGE = 'about.html'
SHOW_DATE_MODIFIED = False
SHOW_SERIES = False
SHOW_ARTICLE_CATEGORY = False
PDF_PROCESSOR = False

# Menu items
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVE_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
DISPLAY_SOCIAL_ON_MENU = True
MENUITEMS = (('Projects', '/projects'),
             ('Blog', '/blog.html'),
             ('Media', '/media'),
             ('About', '/about'),
            )

# Sidebar options
DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = False
DISPLAY_SERIES_ON_SIDEBAR = False
DISPLAY_SOCIAL_ON_SIDEBAR = False
DISPLAY_ARCHIVE_ON_SIDEBAR = True
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/TableTopSec'),
          ('youtube', 'https://www.youtube.com/user/TableTopSecurity'),
          ('flickr', 'https://www.flickr.com/tabletopsecurity'),
          ('boardgamegeek', 'https://boardgamegeek.com/boardgamepublisher/23997/tabletop-security'),
          ('google-plus', 'https://plus.google.com/114066012466458862886'),
          ('github', 'http://github.com/tabletopsecurity')
         )


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme related settings
THEME = 'themes/pelican-bootstrap3'
THEME_STATIC_PATHS=['static']
CSS_FILE='tts.css'
CUSTOM_CSS = 'static/tts.css'

# Caching
LOAD_CONTENT_CACHE = False
