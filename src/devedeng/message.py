# Copyright 2014 (C) Raster Software Vigo (Sergio Costas)
#
# This file is part of DeVeDe-NG
#
# DeVeDe-NG is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# DeVeDe-NG is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from gi.repository import Gtk
import os
import devedeng.configuration_data

class message_window:

    def __init__(self,text,title,list_data = None):

        self.config = devedeng.configuration_data.configuration.get_config()

        builder = Gtk.Builder()
        builder.set_translation_domain(self.config.gettext_domain)

        builder.add_from_file(os.path.join(self.config.glade,"wmessage.ui"))
        builder.connect_signals(self)
        wmessage_window = builder.get_object("dialog_message")
        wmessage_window.set_title(title)
        wmessage_text = builder.get_object("label_message")
        wmessage_text.set_markup(text)
        wmessage_list = builder.get_object("list_message")
        wmessage_liststore = builder.get_object("liststore_elements")
        wmessage_window.show_all()

        if (list_data is None):
            wmessage_list.hide()
        else:
            for element in list_data:
                wmessage_liststore.append([element])

        wmessage_window.run()
        wmessage_window.destroy()
