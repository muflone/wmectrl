##
#     Project: wmectrl
# Description: An enhanced window manager control
#      Author: Fabio Castelli (Muflone) <muflone@muflone.com>
#   Copyright: 2010-2025 Fabio Castelli
#     License: GPL-3+
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
##

import utils

def activate(window):
  "Activate the window"
  window.activate(utils.timestamp())

def move_to_workspace(window, workspace):
  "Move the window to the workspace"
  window.move_to_workspace(workspace)

def set_above(window, status):
  "Set or unset the selected window above others"
  if status==utils.TRUE:
    window.make_above()
  elif status==utils.FALSE:
    window.unmake_above()

def set_below(window, status):
  "Set or unset the selected window below others"
  if status==utils.TRUE:
    window.make_below()
  elif status==utils.FALSE:
    window.unmake_below()

def set_minimize(window, status):
  "Set or unset the selected window minimized"
  if status==utils.TRUE:
    window.minimize()
  elif status==utils.FALSE:
    window.unminimize(utils.timestamp())

def set_maximize(window, status):
  "Set or unset the selected window maximized"
  if status==utils.TRUE:
    window.maximize()
  elif status==utils.FALSE:
    window.unmaximize()

def set_maximize_horizontally(window, status):
  "Set or unset the selected window maximized horizontally"
  if status==utils.TRUE:
    window.maximize_horizontally()
  elif status==utils.FALSE:
    window.unmaximize_horizontally()

def set_maximize_vertically(window, status):
  "Set or unset the selected window maximized vertically"
  if status==utils.TRUE:
    window.maximize_vertically()
  elif status==utils.FALSE:
    window.unmaximize_vertically()

def set_pin(window, status):
  "Set or unset the selected window pinned"
  if status==utils.TRUE:
    window.pin()
  elif status==utils.FALSE:
    window.unpin()

def set_shade(window, status):
  "Set or unset the selected window shaded"
  if status==utils.TRUE:
    window.shade()
  elif status==utils.FALSE:
    window.unshade()

def set_sticky(window, status):
  "Set or unset the selected window sticky"
  if status==utils.TRUE:
    window.stick()
  elif status==utils.FALSE:
    window.unstick()

def set_fullscreen(window, status):
  "Set or unset the selected window fullscreen"
  if status is not None:
    window.set_fullscreen(status==utils.TRUE and True or False)

def set_skip_pager(window, status):
  "Set or unset the selected window skip pager"
  if status is not None:
    window.set_skip_pager(status==utils.TRUE and True or False)

def set_skip_tasklist(window, status):
  "Set or unset the selected window skip tasklist"
  if status is not None:
    window.set_skip_tasklist(status==utils.TRUE and True or False)

def set_geometry(window, left, top, width, height):
  "Move or resize window"
  if left or top or height or width:
    geometry = window.get_geometry()
    if left is None:
      left = geometry[0]
    if top is None:
      top = geometry[1]
    if width is None:
      width = geometry[2]
    if height is None:
      height = geometry[3]
    window.set_geometry(10, 15, left, top, width, height)

def manual_move(window):
  "Start window move using keyboard/mouse"
  window.keyboard_move()

def manual_resize(window):
  "Start window move using keyboard/mouse"
  window.keyboard_size()

def close(window):
  "Close the selected window"
  window.close(utils.timestamp())
