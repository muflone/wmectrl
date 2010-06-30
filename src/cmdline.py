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

from optparse import OptionParser, OptionGroup
from utils import truefalse, APP_VERSION

def get_cmdline():
  parser = OptionParser(usage='usage: %prog [options]',
    version='%' + 'prog %s' % APP_VERSION)
  parser.add_option('-s', '--screen', action='store', type='int',
    help='select screen number')
  parser.add_option('-S', '--workspace', action='store', type='int',
    help='select workspace number')
  parser.add_option('-w', '--window', action='store', type='string',
    help='select window')
  parser.add_option('-L', '--list-windows', action='store_true',
    help='list all windows title')
  parser.add_option('-I', '--show-information', action='store_true',
    help='show information about selected screen')
  parser.add_option('--exact-title', action='store_true',
    help='select window by exact title')
  parser.add_option('--exact-pid', action='store_true',
    help='select window by exact pid')
  parser.add_option('--exact-app-title', action='store_true',
    help='select window by application title')

  group = OptionGroup(parser, 'Workspace control')
  parser.add_option_group(group)
  group.add_option('-d', '--show-desktop', action='store_true',
    help='show the desktop')
  group.add_option('--set-workspaces-count', action='store', type='int',
    help='change the number of workspaces')
  group.add_option('--set-workspace-name', action='store', type='string',
    help='change the workspace name')
  group.add_option('--set-workspace-active', action='store_true',
    help='change the active workspace')

  group = OptionGroup(parser, 'Window control')
  parser.add_option_group(group)
  group.add_option('-T', '--move-to', action='store_true',
    help='move the the window to the selected workspace')
  group.add_option('-A', '--activate', action='store_true',
    help='activate the selected window')
  group.add_option('-C', '--close', action='store_true',
    help='close the selected window')
  group.add_option('-P', '--pin', action='store', choices=truefalse,
    help='pin/unpin the window')
  group.add_option('-G', '--skip-pager', action='store', choices=truefalse,
    help='set/unset skip pager for the window')
  group.add_option('-K', '--skip-tasklist', action='store', choices=truefalse,
    help='set/unset skip tasklist for the window')
  group.add_option('-D', '--shade', action='store', choices=truefalse,
    help='shade/unshade the window')
  group.add_option('-J', '--sticky', action='store', choices=truefalse,
    help='stick/unstick the window')

  group = OptionGroup(parser, 'Window position')
  parser.add_option_group(group)
  group.add_option('-E', '--above', action='store', choices=truefalse,
    help='set/unset the window above others')
  group.add_option('-B', '--below', action='store', choices=truefalse,
    help='set/unset the window below others')
  group.add_option('-U', '--manual-move', action='store_true',
    help='start manual window move using keyboard/mouse')
  group.add_option('-X', '--left', action='store', type='int',
    help='set left/X position of the window')
  group.add_option('-Y', '--top', action='store', type='int',
    help='set top/Y position of the window')

  group = OptionGroup(parser, 'Window size')
  parser.add_option_group(group)
  group.add_option('-N', '--minimized', action='store', choices=truefalse,
    help='minimize/unminimize the window')
  group.add_option('-M', '--maximized', action='store', choices=truefalse,
    help='maximize/unmaximize the window')
  group.add_option('-O', '--horizontally', action='store', choices=truefalse,
    help='maximize/unmaximize horizontally the window')
  group.add_option('-V', '--vertically', action='store', choices=truefalse,
    help='maximize/unmaximize vertically the window')
  group.add_option('-W', '--width', action='store', type='int',
    help='set width of the window')
  group.add_option('-H', '--height', action='store', type='int',
    help='set height of the window')
  group.add_option('-F', '--fullscreen', action='store', choices=truefalse,
    help='fullscreen/unfullscreen the window')
  group.add_option('-R', '--manual-resize', action='store_true',
    help='start manual window resize using keyboard/mouse')

  options, args = parser.parse_args()
  return options, args, parser
