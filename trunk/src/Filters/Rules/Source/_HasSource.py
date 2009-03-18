#
# Gramps - a GTK+/GNOME based genealogy program
#
# Copyright (C) 2002-2006  Donald N. Allingham
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

# $Id: _HasSource.py 9912 2008-01-22 09:17:46Z acraphae $

#-------------------------------------------------------------------------
#
# Standard Python modules
#
#-------------------------------------------------------------------------
from gettext import gettext as _

#-------------------------------------------------------------------------
#
# GRAMPS modules
#
#-------------------------------------------------------------------------
from Filters.Rules._Rule import Rule

#-------------------------------------------------------------------------
#
# HasEvent
#
#-------------------------------------------------------------------------
class HasSource(Rule):
    """Rule that checks for a person with a particular value"""


    labels      = [ _('Title:'), 
                    _('Author:'), 
                    _('Publication:') ]
    name        = _('Sources matching parameters')
    description = _("Matches sources with particular parameters")
    category    = _('General filters')

    def apply(self,db,source):
        if not self.match_substring(0,source.get_title()):
            return False

        if not self.match_substring(1,source.get_author()):
            return False

        if not self.match_substring(2,source.get_publication_info()):
            return False

        return True