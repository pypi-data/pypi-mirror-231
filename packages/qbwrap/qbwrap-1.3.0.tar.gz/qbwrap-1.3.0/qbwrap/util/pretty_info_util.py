#!/usr/bin/env python3


"""

""" """

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""


from colorama import Fore
from colorama import Style


class PrettyInfoUtil:
    """! Pretty info util."""

    @staticmethod
    def print(main_message: str, sub_message: str = "", message_type: str = "info"):
        """!
        Print a message.

        As last argument any standard keyword arguments of the Python built-in
        print method are accepted.
        """

        if message_type == "warn":
            star_color = Fore.YELLOW
        elif message_type == "err":
            star_color = Fore.RED
        else:
            star_color = Fore.GREEN

        print(
            f" {Style.BRIGHT}"
            + f"{star_color}*{Fore.RESET}"
            + f" {main_message}{Style.RESET_ALL}"
            f" {sub_message}",
        )
