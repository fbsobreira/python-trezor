# This file is part of the Trezor project.
#
# Copyright (C) 2012-2018 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import pytest

from trezorlib import debuglink, tron
from trezorlib.tools import parse_path

from .common import TrezorTest


@pytest.mark.tron
class TestMsgTronGetaddress(TrezorTest):
    def test_tron_getaddressAllAllAll(self):
        self.setup_mnemonic_allallall()

        assert (
            tron.get_address(self.client, parse_path("m/44'/195'/0'/0/0"))
            == "TY72iA3SBtrds3QLYsS7LwYfkzXwAXCRWT"
        )
        assert (
            tron.get_address(self.client, parse_path("m/44'/195'/1'/0/0"))
            == "TNPgkSKfz2xS39fcyfrouz7QPbkkJaDLYv"
        )
        assert (
            tron.get_address(self.client, parse_path("m/44'/195'/1'/0/1"))
            == "TFgADKfQF6nUZjrumi2qW3XugZ2sJ7Yf2i"
        )

    def test_tron_getaddress(self):
        debuglink.load_device_by_mnemonic(
            self.client,
            mnemonic="abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
            pin="",
            passphrase_protection=False,
            label="test",
            language="english",
        )

        assert (
            tron.get_address(self.client, parse_path("m/44'/195'/0'/0/0"))
            == "TUEZSdKsoDHQMeZwihtdoBiN46zxhGWYdH"
        )
        assert (
            tron.get_address(self.client, parse_path("m/44'/195'/1'/0/0"))
            == "TLrpNTBuCpGMrB9TyVwgEhNVRhtWEQPHh4"
        )
        assert (
            tron.get_address(self.client, parse_path("m/44'/195'/2'/0/0"))
            == "TZJ9qkoxUB1SGdbtChgAjUphBmkJwAeBaW"
        )
        assert (
            tron.get_address(self.client, parse_path("m/44'/195'/1'/0/1"))
            == "TUT9qMmtJtnjJhpazPaLraWSTaThhBpWyR"
        )
