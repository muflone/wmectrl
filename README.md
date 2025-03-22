# wmectrl

[![CircleCI Build Status](https://img.shields.io/circleci/project/github/muflone/wmectrl/master.svg)](https://circleci.com/gh/muflone/wmectrl)

**Description:** An enhanced window manager control

**Copyright:** 2010-2025 Fabio Castelli (Muflone) <muflone@muflone.com>

**License:** GPL-3+

**Source code:** https://github.com/muflone/wmectrl/

**Documentation:** http://www.muflone.com/wmectrl/

# Description

An enhanced window manager control.

# System Requirements

* Python >= 3.9 (developed and tested for Python 3.13)
* GTK+ 3.0 libraries for Python 3
* GObject libraries for Python 3 ( https://pypi.org/project/PyGObject/ )

# Installation

A distutils installation script is available to install from the sources.

To install in your system please use:

    cd /path/to/folder
    python3 setup.py install

To install the files in another path instead of the standard /usr prefix use:

    cd /path/to/folder
    python3 setup.py install --root NEW_PATH

# Usage

If the application is not installed please use:

    cd /path/to/folder
    python3 -m wmectrl.main --help

If the application was installed simply use the `wmectrl --help` command.
