#!/usr/bin/env python

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

from distutils.core import setup
from distutils.command.install_data import install_data
from glob import glob
import os

class InstallData(install_data):
  def run (self):
    install_data.run(self)

setup(
  name='wmectrl',
  version='0.1',
  description='An enhanced window manager control',
  author='Fabio Castelli',
  author_email='muflone@vbsimple.net',
  url='http://code.google.com/p/wmectrl/',
  license='GPL v2',
  data_files=[
    ('share/wmectrl/src', glob('src/*.py'))
  ],
  cmdclass={'install_data': InstallData}
)
