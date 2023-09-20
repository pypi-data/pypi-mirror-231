#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from ..dto.field_dto import FieldDTO
from .base_stanza import BaseStanza


class UserStanza(BaseStanza):
    """! User stanza"""

    def __init__(self):
        super().__init__(stanza_name="user")

        self._fields.add_field(FieldDTO("uid", int))
        self._fields.add_field(FieldDTO("gid", int))

        self._bind_fields()

    def get_user_identifier(self):
        """! Return user.uid."""

        return self._get_field_data("uid")

    def get_group_identifier(self):
        """! Return user.gid."""

        return self._get_field_data("uid")
