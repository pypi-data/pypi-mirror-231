#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from ..dto.field_dto import FieldDTO
from .base_stanza import BaseStanza


class UnshareStanza(BaseStanza):
    """! Unshare stanza"""

    def __init__(self):
        super().__init__(stanza_name="unshare")

        self._fields.add_field(FieldDTO("user", bool))
        self._fields.add_field(FieldDTO("user_try", bool))
        self._fields.add_field(FieldDTO("ipc", bool))
        self._fields.add_field(FieldDTO("pid", bool))
        self._fields.add_field(FieldDTO("net", bool))
        self._fields.add_field(FieldDTO("uts", bool))
        self._fields.add_field(FieldDTO("cgroup", bool))
        self._fields.add_field(FieldDTO("cgroup_try", bool))
        self._fields.add_field(FieldDTO("all", bool))

        self._bind_fields()

    def is_unshared(self, unshare_name: str) -> bool:
        """!
        Return whether a given unshare_name is unshared.

        @param unshare_name: a Linux unshare method
        @return whether a given unshare method is desired
        """

        for data_key in self._fields.get_field_names():
            if data_key == unshare_name:
                return self._get_field_data(unshare_name)

        raise RuntimeError(
            f"is_unshared: wrong unshare_name, given '{unshare_name}'"
        )
