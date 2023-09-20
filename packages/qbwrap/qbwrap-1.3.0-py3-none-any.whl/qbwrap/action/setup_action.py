#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from ..dao.argument_parser_dao import ArgumentParserDAO
from ..dao.qbwrap_setup_dao import QBwrapSetupDAO

from ..dto.run_action_options_dto import RunActionOptionsDTO

from .run_action import RunAction


class SetupAction:
    """! Setup action."""

    def __init__(
        self,
        argument_parser: ArgumentParserDAO,
        qbwrap_setup: QBwrapSetupDAO,
    ):
        self.__qbwrap_setup = qbwrap_setup

        run_action_options = RunActionOptionsDTO(
            qbwrap_setup.get_setup_stanza().get_privileged(),
            argument_parser.get_become_root_method(),
            argument_parser.get_fake(),
            argument_parser.get_quiet(),
        )

        self.__mkdir_run_action = RunAction(
            ["mkdir", "-p", qbwrap_setup.get_location()],
            run_action_options,
        )
        self.__url_download_run_action = RunAction(
            qbwrap_setup.get_download_command(),
            run_action_options,
        )
        self.__archive_extraction_run_action = RunAction(
            qbwrap_setup.get_extraction_command(),
            run_action_options,
        )

    def execute(self):
        """! Execute the Setup action."""

        self.__mkdir_run_action.execute()
        self.__url_download_run_action.execute()

        self.__qbwrap_setup.verify_archive()

        self.__archive_extraction_run_action.execute()
