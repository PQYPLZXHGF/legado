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

# $Id: _RepoRefModel.py 9912 2008-01-22 09:17:46Z acraphae $

#-------------------------------------------------------------------------
#
# GTK libraries
#
#-------------------------------------------------------------------------
import gtk

#-------------------------------------------------------------------------
#
# GRAMPS classes
#
#-------------------------------------------------------------------------


#-------------------------------------------------------------------------
#
# RepoRefModel
#
#-------------------------------------------------------------------------
class RepoRefModel(gtk.ListStore):

    def __init__(self, ref_list, db):
        gtk.ListStore.__init__(self, str, str, str, str, object)
        self.db = db
        for ref in ref_list:
            repo = self.db.get_repository_from_handle(ref.ref)
            self.append(row=[
                repo.gramps_id,
                repo.name,
                ref.call_number, 
                str(repo.get_type()),
                ref, ])