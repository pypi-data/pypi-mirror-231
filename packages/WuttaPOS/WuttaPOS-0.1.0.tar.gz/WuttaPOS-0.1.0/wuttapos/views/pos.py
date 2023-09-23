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
WuttaPOS - POS view
"""

import flet as ft

from .base import WuttaView


class POSView(WuttaView):
    """
    Main POS view for WuttaPOS
    """

    def build_controls(self):

        self.main_input = ft.TextField(on_submit=self.main_submit,
                                       autofocus=True)

        def make_text(*args, **kwargs):
            kwargs['weight'] = ft.FontWeight.BOLD
            kwargs['size'] = 20
            return ft.Text(*args, **kwargs)

        return [
            self.build_header(),

            ft.Row(
                [self.main_input],
                alignment=ft.MainAxisAlignment.CENTER,
            ),

            ft.Row(),
            ft.Row(),
            ft.Row(),

            ft.Row(
                [ft.Text("TODO: need lots of things yet here...somewhere..")],
                alignment=ft.MainAxisAlignment.CENTER,
            ),

            ft.Row(
                [ft.Text("TODO: for instance, items rang up might go here")],
            ),

            ft.DataTable(
                columns=[
                    ft.DataColumn(make_text("UPC")),
                    ft.DataColumn(make_text("Description")),
                    ft.DataColumn(make_text("Price"), numeric=True),
                ],
                rows=[
                    ft.DataRow(
                        cells=[
                            ft.DataCell(make_text("0007430500132-1")),
                            ft.DataCell(make_text("Apple Cider Vinegar 32oz")),
                            ft.DataCell(make_text("$5.99")),
                        ],
                    ),
                    ft.DataRow(
                        cells=[
                            ft.DataCell(make_text("0007430500116-1")),
                            ft.DataCell(make_text("Apple Cider Vinegar 16oz")),
                            ft.DataCell(make_text("$3.59")),
                        ],
                    ),
                ],
            ),
        ]

    def main_submit(self, e):
        value = self.main_input.value.upper()
        self.page.snack_bar = ft.SnackBar(ft.Text(f"submit: {value}", color='black',
                                                  weight=ft.FontWeight.BOLD),
                                          bgcolor='yellow',
                                          duration=1500)
        self.page.snack_bar.open = True
        self.main_input.value = ""
        self.main_input.focus()
        self.page.update()
