#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from typing import Any

from ..dao.fields_dao import FieldsDAO
from ..dao.stanza_data_dao import StanzaDataDAO

from ..util.pretty_info_util import PrettyInfoUtil


class BaseStanza:
    """! Base stanza."""

    def __init__(self, stanza_name: str):
        self.__stanza_name = stanza_name

        self.__stanza_data = StanzaDataDAO()

        self._fields = FieldsDAO()

    def _bind_fields(self):
        """! Create base field bindings."""

        for field in self._fields.get_fields():
            self.__stanza_data.set_data(field.get_name(), False)

    def load_dict_data(self, data_dict: dict):
        """! Load fields form data_dict."""

        if self.__stanza_name not in data_dict:
            PrettyInfoUtil.print(
                main_message="No data was loaded for stanza:",
                sub_message=self.__stanza_name,
                message_type="warn",
            )

            return

        stanza_dict = data_dict[self.__stanza_name]

        for field in self.get_fields().get_fields():
            field_name = field.get_name()
            field_type = field.get_type()

            if field_name in stanza_dict:
                field_data = stanza_dict[field_name]

                if isinstance(field_data, field_type):
                    self.__stanza_data.set_data(field_name, field_data)

                else:
                    raise RuntimeError(
                        "load_dict_data: incorrect field type "
                        + f'for field "{field_name}", '
                        + f"given {field_data} but "
                        + f"required type was {field_type}"
                    )

    def _get_field_data(self, field_name: str) -> Any:
        """! Return data of a field field_name."""

        return self.__stanza_data.get_data(field_name)

    def get_fields(self) -> FieldsDAO:
        """! Get fields."""

        return self._fields
