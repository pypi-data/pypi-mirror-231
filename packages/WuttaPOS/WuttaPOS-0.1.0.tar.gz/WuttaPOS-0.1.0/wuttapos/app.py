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
WuttaPOS app
"""

import json
import os

from rattail.config import make_config

import flet as ft

import wuttapos


def main(page: ft.Page):
    config = make_config()

    page.title = f"WuttaPOS v{wuttapos.__version__}"
    page.window_full_screen = True
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # nb. track current user, txn etc.
    page.shared = {}

    # TODO: this may be too hacky but is useful for now/dev
    if not config.production():
        path = os.path.join(config.appdir(), '.wuttapos.cache')
        if os.path.exists(path):
            with open(path, 'rt') as f:
                page.shared = json.loads(f.read())

    def clean_exit():
        if not config.production():
            # TODO: this may be too hacky but is useful for now/dev
            path = os.path.join(config.appdir(), '.wuttapos.cache')
            with open(path, 'wt') as f:
                f.write(json.dumps(page.shared))
        page.window_destroy()

    def keyboard(e):
        # exit on ctrl+Q
        if e.ctrl and e.key == 'Q':
            if not e.shift and not e.alt and not e.meta:
                clean_exit()

    page.on_keyboard_event = keyboard

    def window_event(e):
        if e.data == 'close':
            clean_exit()

    # cf. https://flet.dev/docs/controls/page/#window_destroy
    page.window_prevent_close = True
    page.on_window_event = window_event

    # TODO: probably these should be auto-loaded from spec
    from wuttapos.views.pos import POSView
    from wuttapos.views.login import LoginView

    # cf .https://flet.dev/docs/guides/python/navigation-and-routing#building-views-on-route-change

    def route_change(route):
        page.views.clear()
        if page.route == '/pos':
            page.views.append(POSView(config, '/pos'))
        elif page.route == '/login':
            page.views.append(LoginView(config, '/login'))
        page.update()

    # TODO: this was in example docs but not sure what it's for?
    # def view_pop(view):
    #     page.views.pop()
    #     top_view = page.views[-1]
    #     page.go(top_view.route)

    page.on_route_change = route_change
    # page.on_view_pop = view_pop

    # TODO: this may be too hacky but is useful for now/dev
    if not config.production() and page.shared.get('user_uuid'):
        page.go('/pos')
    else:
        page.go('/login')


# TODO: can we inject config to the main() via ft.app() kwargs somehow?
# pretty sure the `wuttapos open` command is trying to anyway..
def run_app(config=None):
    ft.app(target=main)


if __name__ == '__main__':
    run_app()
