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
WuttaPOS - flet views (base class)
"""

import flet as ft

from wuttapos.controls.header import WuttaHeader


class WuttaView(ft.View):
    """
    Base class for all Flet views used in WuttaPOS
    """

    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config = config
        self.app = self.config.get_app()
        self.model = self.app.model

        controls = self.build_controls()
        self.controls = [
            WuttaViewContainer(self.config,
                               content=ft.Column(controls=controls),
                               expand=True),
        ]

    def build_controls(self):
        return [self.build_header()]

    def build_header(self):
        return WuttaHeader(self.config)


class WuttaViewContainer(ft.Container):
    """
    Main container class to wrap all controls for a view.  Used for
    displaying background image etc.
    """

    def __init__(self, config, *args, **kwargs):
        self.config = config

        if 'image_src' not in kwargs and not self.config.production():
            # TODO: host a local testing image? where *should* this come from?
            image = self.config.get('rattail', 'testing_watermark')
            if image:
                kwargs['image_src'] = image
                kwargs.setdefault('image_repeat', ft.ImageRepeat.REPEAT)

        super().__init__(*args, **kwargs)
