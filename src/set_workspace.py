##
#   Project: wmectrl - An enhanced window manager control
#    Author: Fabio Castelli <muflone@vbsimple.net>
# Copyright: 2010 Fabio Castelli
#   License: GPL-2+
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
# 
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
# 
# On Debian GNU/Linux systems, the full text of the GNU General Public License
# can be found in the file /usr/share/common-licenses/GPL-2.
##

import utils

def activate(workspace):
  "Activate the workspace"
  workspace.activate(utils.timestamp())

def set_name(workspace, name):
  "Set the workspace name"
  workspace.change_name(name)

def set_count(screen, count):
  "Set the workspace count"
  screen.change_workspace_count(count)
