# -*- coding: utf-8; -*-
################################################################################
#
#  WuttaPOS -- Pythonic Point of Sale System
#  Copyright © 2023 Lance Edgar
#
#  This file is part of WuttaPOS.
#
#  WuttaPOS is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  WuttaPOS is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
#  FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
#  details.
#
#  You should have received a copy of the GNU General Public License along with
#  WuttaPOS.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
"""
WuttaPOS commands
"""

import sys

from rattail import commands

from wuttapos import __version__


def main(*args):
    """
    Main entry point for WuttaPOS command system
    """
    args = list(args or sys.argv[1:])
    cmd = Command()
    cmd.run(*args)


class Command(commands.Command):
    """
    Top-level command for WuttaPOS
    """
    name = 'wuttapos'
    version = __version__
    description = "WuttaPOS (point of sale)"
    long_description = ''


class Open(commands.Subcommand):
    """
    Open the Point of Sale app
    """
    name = 'open'
    description = __doc__.strip()

    def run(self, args):
        from wuttapos.app import run_app

        run_app(self.config)


class Status(commands.Subcommand):
    """
    Show status of the POS lane
    """
    name = 'status'
    description = __doc__.strip()

    def run(self, args):
        print("TODO: show status")
