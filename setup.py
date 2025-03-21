#!/usr/bin/env python
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
