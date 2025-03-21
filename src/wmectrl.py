#!/usr/bin/python
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

import wnck
import cmdline
import info
import set_window
import set_workspace

options, args, parser = cmdline.get_cmdline()

# Select default or specified screen
if options.screen is None:
  screen = wnck.screen_get_default()
  if screen is None:
    parser.error('default screen not found')
else:
  screen = wnck.screen_get(options.screen)
  if screen is None:
    parser.error('invalid screen number: %d' % options.screen)

# Change workspaces count
if options.set_workspaces_count is not None:
  set_workspace.set_count(screen, options.set_workspaces_count)

# Update workspaces/windows list
screen.force_update()

# Select active or specified workspace
if options.workspace is None:
  ws = screen.get_active_workspace()
  if ws is None:
    parser.error('active workspace not found')
else:
  ws = screen.get_workspace(options.workspace)
  if ws is None:
    parser.error('invalid workspace number: %d' % options.workspace)

# Change workspace name
if options.set_workspace_name is not None:
  set_workspace.set_name(ws, options.set_workspace_name)

# Change active workspace
if options.set_workspace_active is not None:
  set_workspace.activate(ws)

# Show desktop action
if options.show_desktop is not None:
  screen.toggle_showing_desktop(True)

# Select active or specified window
if options.window is None:
  # Use active window
  win = screen.get_active_window()
  if win is None:
    parser.error('active window not found')
else:
  # Search for a window
  for win in screen.get_windows():
    if options.exact_title:
      # Search for exact title
      if options.window == win.get_name():
        break
    elif options.exact_pid:
      # Search for exact PID
      if int(options.window) == win.get_pid():
        break
    elif options.exact_app_title:
      # Search for exact application title
      if options.window == win.get_application().get_name():
        break
    else:
      # Search for contained title
      if options.window in win.get_name():
        break
  else:
    # Window not found
    win = None
  if win is None:
    parser.error('window not found: %s' % options.window)

# Close selected window
if options.activate is not None:
  set_window.activate(win)

# Move window to the workspace
if options.move_to is not None:
  set_window.move_to_workspace(win, ws)

set_window.set_above(win, options.above)
set_window.set_below(win, options.below)
set_window.set_minimize(win, options.minimized)
set_window.set_maximize(win, options.maximized)
set_window.set_maximize_horizontally(win, options.horizontally)
set_window.set_maximize_vertically(win, options.vertically)
set_window.set_pin(win, options.pin)
set_window.set_shade(win, options.shade)
set_window.set_sticky(win, options.sticky)
set_window.set_fullscreen(win, options.fullscreen)
set_window.set_skip_pager(win, options.skip_pager)
set_window.set_skip_tasklist(win, options.skip_tasklist)
set_window.set_geometry(win, options.left, options.top, options.width, options.height)

# Move window with the keyboard/mouse
if options.manual_move is not None:
  set_window.manual_move(win)

# Resize window with the keyboard/mouse
if options.manual_resize is not None:
  set_window.manual_resize(win)

# Show screen information
if options.show_information is not None:
  info.print_info(screen, ws, win)

# Close selected window
if options.close is not None:
  set_window.close(win)

# List all windows
if options.list_windows is not None:
  for window in screen.get_windows():
    print window.get_pid(), window.get_name()
