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

def print_info(screen, ws, window):
  print 'screen number:          %d' % screen.get_number()
  print 'screen size:            %dx%d' % (screen.get_width(), screen.get_height())
  print 'WM name:                %s' % screen.get_window_manager_name()
  print 'showing desktop:        %s' % screen.get_showing_desktop()
  print 'windows count:          %d' % len(screen.get_windows())
  print 'selected window:        %s (%d)' % (window.get_name(), window.get_pid())
  geometry = window.get_geometry()
  print 'window position:        %d,%d' % (geometry[0], geometry[1])
  print 'window size:            %dx%d' % (geometry[2], geometry[3])
  geometry = window.get_client_window_geometry()
  print 'window client position: %d,%d' % (geometry[0], geometry[1])
  print 'window client size:     %dx%d' % (geometry[2], geometry[3])
  print 'window active:          %s' % window.is_active()
  print 'window above:           %s' % window.is_above()
  print 'window below:           %s' % window.is_below()
  print 'window fullscreen:      %s' % window.is_fullscreen()
  print 'window minimized:       %s' % window.is_minimized()
  print 'window maximized:       %s' % window.is_maximized()
  print 'window maximized H:     %s' % window.is_maximized_horizontally()
  print 'window maximized V:     %s' % window.is_maximized_vertically()
  print 'window pinned:          %s' % window.is_pinned()
  print 'window shaded:          %s' % window.is_shaded()
  print 'window sticky:          %s' % window.is_sticky()
  print 'window skip pager:      %s' % window.is_skip_pager()
  print 'window skip tasklist:   %s' % window.is_skip_tasklist()
  print 'window in workspace:    %s' % window.is_on_workspace(ws)
  print 'window in viewport:     %s' % window.is_in_viewport(ws)
  print 'window needs attention: %s' % window.needs_attention()
  app = window.get_application()
  print 'window application:     %s (%d)' % (app.get_name(), app.get_pid())
  print 'workspaces count:       %d' % screen.get_workspace_count()
  print 'selected workspace:     %d (%s)' % (ws.get_number(), ws.get_name())
  print 'workspace size:         %dx%d' % (ws.get_width(), ws.get_height())
  print 'workspace layout:       %dx%d' % (
    ws.get_layout_row(), ws.get_layout_column())
  print 'workspace viewport:     %dx%d' % (
    ws.get_viewport_x(), ws.get_viewport_y())
  print 'workspace virtual:      %s' % ws.is_virtual()
