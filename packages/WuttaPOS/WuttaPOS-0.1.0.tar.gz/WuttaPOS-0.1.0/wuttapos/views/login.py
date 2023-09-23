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
WuttaPOS - login view
"""

import flet as ft

from .base import WuttaView


class LoginView(WuttaView):
    """
    Main POS view for WuttaPOS
    """

    def __init__(self, *args, **kwargs):

        # TODO: maybe support setting this to False?  for now that's not 100% supported
        self.show_username = kwargs.pop('show_username', True)

        super().__init__(*args, **kwargs)

    def build_controls(self):
        controls = [
            ft.Row(
                [ft.Text(value="Welcome to WuttaPOS", weight=ft.FontWeight.BOLD, size=28)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(),
            ft.Row(),
            ft.Row(),
        ]

        if self.show_username:
            self.username = ft.TextField(label="Login", width=200,
                                         on_submit=self.username_submit,
                                         autofocus=True)
            controls.extend([
                ft.Row(
                    [self.username],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ])

        self.password = ft.TextField(label="Password", width=200, password=True,
                                     on_submit=self.password_submit,
                                     autofocus=not self.show_username)

        controls.extend([
            ft.Row(
                [self.password],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    ft.FilledButton("Login", on_click=self.attempt_login),
                    ft.ElevatedButton("Clear", on_click=self.clear_login),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(),
            ft.Row(
                [ft.Text("TODO: should have on-screen keyboard (at least 10-key pad?) "
                            "for use with login etc.", italic=True)],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ])

        return [
            self.build_header(),
            ft.Column(controls=controls,
                      expand=True,
                      alignment=ft.MainAxisAlignment.CENTER),
        ]

    def username_submit(self, e):
        if self.username.value:
            self.password.focus()
        else:
            self.username.focus()

    def password_submit(self, e):
        if self.password.value:
            self.attempt_login()
        else:
            self.password.focus()

    def clear_login(self, e):
        if self.show_username:
            self.username.value = ""
        self.password.value = ""
        if self.show_username:
            self.username.focus()
        else:
            self.password.focus()
        self.page.update()

    def attempt_login(self, e=None):
        if self.show_username and not self.username.value:
            self.username.focus()
            return
        if not self.password.value:
            self.password.focus()
            return

        session = self.app.make_session()
        auth = self.app.get_auth_handler()
        user = auth.authenticate_user(session, self.username.value, self.password.value)
        user_display = str(user) if user else None
        session.close()

        if user:
            # handle success
            self.page.shared.update({
                'user_uuid': user.uuid,
                'user_display': user_display,
            })
            self.page.go('/pos')

        else:
            # handle failure
            self.page.snack_bar = ft.SnackBar(ft.Text("Login failed!",
                                                      color='black',
                                                      weight=ft.FontWeight.BOLD),
                                              bgcolor='yellow',
                                              duration=1500)
            self.page.snack_bar.open = True
            self.password.focus()
            self.page.update()
