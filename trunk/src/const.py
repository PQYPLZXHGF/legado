#                                                     -*- python -*-
#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2000-2006  Donald N. Allingham
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#

# $Id: const.py.in 10692 2008-05-08 12:06:39Z pez4brian $

"""
Provides constants for other modules
"""

#-------------------------------------------------------------------------
#
# Standard python modules
#
#-------------------------------------------------------------------------
import os
import sys
from gettext import gettext as _

#-------------------------------------------------------------------------
#
# Standard GRAMPS Websites
#
#-------------------------------------------------------------------------
URL_HOMEPAGE    = "http://gramps-project.org/"
URL_MAILINGLIST = "http://sourceforge.net/mail/?group_id=25770"
URL_BUGTRACKER  = "http://bugs.gramps-project.org/bug_report_advanced_page.php"
URL_WIKISTRING  = "http://gramps-project.org/wiki/index.php?title="
URL_MANUAL_PAGE = "Gramps_3.0_Wiki_Manual"
WIKI_FAQ = "FAQ"
WIKI_KEYBINDINGS = "Gramps_3.0_Wiki_Manual_-_Keybindings"
WIKI_EXTRAPLUGINS= "3.0.x_Third-party_Plugins"

#-------------------------------------------------------------------------
#
# Mime Types
#
#-------------------------------------------------------------------------
APP_FAMTREE     = 'x-directory/normal'
APP_GRAMPS      = "application/x-gramps"
APP_GRAMPS_XML  = "application/x-gramps-xml"
APP_GEDCOM      = "application/x-gedcom"
APP_GRAMPS_PKG  = "application/x-gramps-package"
APP_GENEWEB     = "application/x-geneweb"
APP_VCARD       = ["text/x-vcard", "text/x-vcalendar"]

#-------------------------------------------------------------------------
#
# system paths
#
#-------------------------------------------------------------------------
PREFIXDIR = "@prefix@"
SYSCONFDIR = "@sysconfdir@"

#-------------------------------------------------------------------------
#
# Determine the home directory. According to Wikipedia, most UNIX like
# systems use HOME. I'm assuming that this would apply to OS X as well.
# Windows apparently uses USERPROFILE
#
#-------------------------------------------------------------------------
if os.environ.has_key('GRAMPSHOME'):
    USER_HOME = os.environ['GRAMPSHOME'] 
    HOME_DIR = os.path.join(USER_HOME, 'gramps')
elif os.environ.has_key('USERPROFILE'):
    USER_HOME = os.environ['USERPROFILE'] 
    if os.environ.has_key('APPDATA'):
        HOME_DIR = os.path.join(os.environ['APPDATA'], 'gramps')
    else:
        HOME_DIR = os.path.join(USER_HOME, 'gramps')
else:
    USER_HOME = os.environ['HOME'] 
    HOME_DIR = os.path.join(USER_HOME, '.gramps')

#-------------------------------------------------------------------------
#
# Paths to files - assumes that files reside in the same directory as
# this one, and that the plugins directory is in a directory below this.
#
#-------------------------------------------------------------------------
# test for sys.frozen to detect a py2exe executable on Windows
if hasattr(sys, "frozen"):
    ROOT_DIR = os.path.abspath(os.path.dirname(
        unicode(sys.executable, sys.getfilesystemencoding())))
else:
    ROOT_DIR = os.path.abspath(os.path.dirname(
        unicode(__file__, sys.getfilesystemencoding())))

IMAGE_DIR      = os.path.join(ROOT_DIR, "images")

CUSTOM_FILTERS = os.path.join(HOME_DIR, "custom_filters.xml")
REPORT_OPTIONS = os.path.join(HOME_DIR, "report_options.xml")
TOOL_OPTIONS   = os.path.join(HOME_DIR, "tool_options.xml")

ENV_DIR        = os.path.join(HOME_DIR, "env")
TEMP_DIR       = os.path.join(HOME_DIR, "temp")
THUMB_DIR      = os.path.join(HOME_DIR, "thumb")
USER_DOCGEN    = os.path.join(HOME_DIR, "docgen")    
USER_PLUGINS   = os.path.join(HOME_DIR, "plugins")    
USER_TEMPLATES = os.path.join(HOME_DIR, "templates")    
# dirs checked/made for each Gramps session
USER_DIRLIST = (HOME_DIR, ENV_DIR, TEMP_DIR, THUMB_DIR,
                USER_DOCGEN, USER_PLUGINS, USER_TEMPLATES)

ICON           = os.path.join(ROOT_DIR, "images", "gramps.png")
LOGO           = os.path.join(ROOT_DIR, "images", "logo.png")
SPLASH         = os.path.join(ROOT_DIR, "images", "splash.jpg")
LICENSE_FILE   = os.path.join(ROOT_DIR, "COPYING")

#
# Glade files
#

GLADE_DIR      = os.path.join(ROOT_DIR, "glade")
GLADE_FILE     = os.path.join(GLADE_DIR, "gramps.glade")
PERSON_GLADE   = os.path.join(GLADE_DIR, "edit_person.glade")
PLUGINS_GLADE  = os.path.join(GLADE_DIR, "plugins.glade")
MERGE_GLADE    = os.path.join(GLADE_DIR, "mergedata.glade")
RULE_GLADE     = os.path.join(GLADE_DIR, "rule.glade")


PLUGINS_DIR    = os.path.join(ROOT_DIR, "plugins")
DOCGEN_DIR     = os.path.join(ROOT_DIR, "docgen")
DATA_DIR       = os.path.join(ROOT_DIR, "data")
SYSTEM_FILTERS = os.path.join(DATA_DIR, "system_filters.xml")
TEMPLATE_DIR   = os.path.join(DATA_DIR, "templates")
TIP_DATA       = os.path.join(DATA_DIR, "tips.xml")

PAPERSIZE      = os.path.join(DATA_DIR, "papersize.xml")

USE_TIPS       = False

if os.sys.platform == "win32":
    USE_THUMBNAILER = False
else:
    USE_THUMBNAILER = True

#-------------------------------------------------------------------------
#
# About box information
#
#-------------------------------------------------------------------------
PROGRAM_NAME   = "GRAMPS"
VERSION        = "@VERSIONSTRING@"
COPYRIGHT_MSG  = u"\u00A9 2001-2006 Donald N. Allingham\n" \
                 u"\u00A9 2007-2008 The GRAMPS Developers"
COMMENTS       = _("GRAMPS (Genealogical Research and Analysis "
                   "Management Programming System) is a personal "
                   "genealogy program.")
AUTHORS        = [
    "Donald N. Allingham", 
    "Alexander Roitman", 
    "Richard Taylor", 
    "Martin Hawlisch", 
    "Brian Matherly", 
    "Tim Waugh", 
    "Donald A. Peterson", 
    "David Hampton", 
    ]
    
AUTHORS_FILE = os.path.join(DATA_DIR, "authors.xml")

DOCUMENTERS    = [
    'Alexander Roitman', 
    ]

TRANSLATORS = _('TRANSLATORS: Translate this to your '
                'name in your native language')

#-------------------------------------------------------------------------
#
# Constants
#
#-------------------------------------------------------------------------
THUMBSCALE   = 96.0
XMLFILE      = "data.gramps"
NO_SURNAME   = "(%s)" % _("none")
NO_GIVEN     = "(%s)" % _("none")

#-------------------------------------------------------------------------
#
# Options Constants
#
#-------------------------------------------------------------------------

# (longName, shortName, type , default, flags, descrip , argDescrip)
POPT_TABLE = [
    ("open",    'O', str, None, 0, "Open family tree",  "FAMILY_TREE"), 
    ("import",  'i', str, None, 0, "Import file",       "FILENAME"), 
    ("output",  'o', str, None, 0, "Write file",        "FILENAME"), 
    ("format",  'f', str, None, 0, 'Specify format',    "FORMAT"), 
    ("action",  'a', str, None, 0, 'Specify action',    "ACTION"), 
    ("options", 'p', str, None, 0, 'Specify options',   "OPTIONS_STRING"), 
    ("debug",   'd', str, None, 0, 'Enable debug logs', "LOGGER_NAME"), 
    ("",        'l', None, None, 0, 'List Family Trees', ""),
    ("force-unlock", 'u', None, None, 0, 'Force unlock of family tree', ""),
]

LONGOPTS = [
    "action=", 
    "class=",
    "debug=",
    "display=",
    "disable-sound", 
    "disable-crash-dialog", 
    "enable-sound",
    "espeaker=",
    "force-unlock",
    "format=",
    "gdk-debug=", 
    "gdk-no-debug=", 
    "gtk-debug=", 
    "gtk-no-debug=", 
    "gtk-module=", 
    "g-fatal-warnings",
    "help",
    "import=", 
    "load-modules=",
    "list" 
    "name=",
    "oaf-activate-iid=", 
    "oaf-ior-fd=", 
    "oaf-private",
    "open=",
    "options=",
    "output=",
    "screen=", 
    "sm-client-id=", 
    "sm-config-prefix=", 
    "sm-disable",
    "sync", 
    "usage",  
    "version", 
]

SHORTOPTS = "O:i:o:f:a:p:d:lhu?"

