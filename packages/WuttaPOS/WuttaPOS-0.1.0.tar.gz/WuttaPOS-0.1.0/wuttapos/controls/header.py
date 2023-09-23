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
WuttaPOS - header control
"""

import flet as ft

from .base import WuttaControl
from .timestamp import WuttaTimestamp


class WuttaHeader(WuttaControl):

    def build(self):
        self.txn_display = ft.Text("Txn: N", weight=ft.FontWeight.BOLD, size=20)
        self.user_display = ft.Text("User: N", weight=ft.FontWeight.BOLD, size=20)
        self.logout_button = ft.FilledButton("Logout", on_click=self.logout_click, visible=False)
        self.logout_divider = ft.VerticalDivider(visible=False)

        controls = [
            self.txn_display,
            ft.VerticalDivider(),
            ft.Text(f"Cust: N", weight=ft.FontWeight.BOLD, size=20),
            ft.VerticalDivider(),
            WuttaTimestamp(self.config, expand=True,
                           weight=ft.FontWeight.BOLD, size=20),
            self.user_display,
            ft.VerticalDivider(),
            self.logout_button,
            self.logout_divider,
            ft.Text(f"WuttaPOS", weight=ft.FontWeight.BOLD, size=20),
        ]

        return ft.Row(controls)

    def did_mount(self):
        self.update_txn_display()
        self.update_user_display()
        self.update()

    def update_txn_display(self):
        txn_display = "N"

        if self.page and self.page.shared and self.page.shared.get('txn_display'):
            txn_display = self.page.shared['txn_display']

        self.txn_display.value = f"Txn: {txn_display}"

    def update_user_display(self):
        user_display = "N"

        if self.page and self.page.shared and self.page.shared.get('user_display'):
            user_display = self.page.shared['user_display']

        self.user_display.value = f"User: {user_display}"

        if self.page and self.page.shared.get('user_uuid'):
            self.logout_button.visible = True
            self.logout_divider.visible = True

    def logout_click(self, e):
        self.page.shared.update({
            'user_uuid': None,
            'user_display': None,
            'txn_display': None,
        })
        self.page.go('/login')
