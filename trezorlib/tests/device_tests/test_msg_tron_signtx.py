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

from binascii import unhexlify

import pytest

from trezorlib import debuglink, messages as proto, tron
from trezorlib.tools import parse_path

from .common import TrezorTest

TRON_DEFAULT_PATH = "m/44'/195'/0'/0/0"


def load_device(self):
    debuglink.load_device_by_mnemonic(
        self.client,
        mnemonic="abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about",
        pin="",
        passphrase_protection=False,
        label="test",
        language="english",
    )


@pytest.mark.tron
@pytest.mark.skip_t1
class TestMsgTronSigntx(TrezorTest):
    def test_tron_send_trx(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("C565"),
            ref_block_hash=bytes.fromhex("6CD623DBE83075D8"),
            expiration=1528768890000,
            timestamp=1528768831987,
            contract=proto.TronContract(
                transfer_contract=proto.TronTransferContract(
                    to_address=bytes.fromhex(
                        "4167E39013BE3CDD3814BED152D7439FB5B6791409"
                    ),
                    amount=1000000,
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "ff4ea446cae4475a500fdfec4019160a42c7bcef4c5b18ab709a74ef9fcb1f405a1ca978a7f783487d3593bf76e1a43c4ed42e201fcf2ebbc90460103c1b768a01"
        )

    def test_tron_send_token(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("E7C3"),
            ref_block_hash=bytes.fromhex("69E2ABB19969F1E7"),
            expiration=1528997142000,
            timestamp=1528997083831,
            contract=proto.TronContract(
                transfer_asset_contract=proto.TronTransferAssetContract(
                    asset_name="CryptoChainToken",
                    to_address=bytes.fromhex(
                        "414F560EB4182CA53757F905609E226E96E8E1A80C"
                    ),
                    amount=1,
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "c3244d575efc0bf11a4a4ac6c24f3d7f195cab200a127382d581a8e4accbf74c2b6f385047350edb00bb4f3455684b2ce6cd73112a7510a2022ebd0201d9b7c700"
        )

    def test_tron_vote_witness(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("906E"),
            ref_block_hash=bytes.fromhex("2597B4DAC069C352"),
            expiration=1530986184000,
            timestamp=1530985887463,
            contract=proto.TronContract(
                vote_witness_contract=proto.TronVoteWitnessContract(
                    votes=[
                        proto.TronVote(
                            vote_address=bytes.fromhex(
                                "4167E39013BE3CDD3814BED152D7439FB5B6791409"
                            ),
                            vote_count=1000000,
                        ),
                        proto.TronVote(
                            vote_address=bytes.fromhex(
                                "41C189FA6FC9ED7A3580C3FE291915D5C6A6259BE7"
                            ),
                            vote_count=100000,
                        ),
                        proto.TronVote(
                            vote_address=bytes.fromhex(
                                "41D49BF5202B3DBA65D46A5BE73396B6B66D3555AA"
                            ),
                            vote_count=10000,
                        ),
                        proto.TronVote(
                            vote_address=bytes.fromhex(
                                "41AD85B8B51C9651F911DA795E4D481DB419C00C6B"
                            ),
                            vote_count=1000,
                        ),
                        proto.TronVote(
                            vote_address=bytes.fromhex(
                                "41D49BF5202B3DBA65D46A5BE73396B6B66D3555AA"
                            ),
                            vote_count=100,
                        ),
                    ]
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "7c1075c0ffecdaafaab98d76de0436e18d028a8a575bd231181f82ea9ce93b367b5d1ff585545ef5e8f1a28578746d346f8e5e8a5e516fc10ce023d3f6ab2ca301"
        )

    def test_tron_witness_create(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                witness_create_contract=proto.TronWitnessCreateContract(
                    url="http://cryptochain.network"
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "692859b8d668ae5146f04512ba97cf2e205b429bcf462a6fa48726be8894be81480e935a3f9d3684cf82e5378d425310066e1ea1b1d99eaebdfa58c32f0cdb8701"
        )

    def test_tron_asset_issue(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                asset_issue_contract=proto.TronAssetIssueContract(
                    name="CryptoChain",
                    abbr="CCT",
                    total_supply=9999999999,
                    frozen_supply=[
                        proto.TronFrozenSupply(frozen_amount=1000, frozen_days=10),
                        proto.TronFrozenSupply(frozen_amount=10000, frozen_days=20),
                        proto.TronFrozenSupply(frozen_amount=100000, frozen_days=30),
                    ],
                    trx_num=100,
                    num=1,
                    start_time=1514764800000,
                    end_time=1546300800000,
                    description="CryptoChain Token Issue Test",
                    url="http://cryptochain.network",
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "861a62e4d0ae920284a5d936220563b5536102b43044103011fc0b523592ef1c3a8a852075d3cce2525c048377b66005f04184d6ec7fe661c0634abc93ba414a00"
        )

    def test_tron_witness_update(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                witness_update_contract=proto.TronWitnessUpdateContract(
                    update_url="http://cryptochain.network"
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "6feca2a4558ded324f439c7cecf596f1378fbd6071569a99ea28f06c4cb1fb754720125f8721c0663e3768b7a888ee8c37fbbb9690e192b8908e225ba49a2aaa01"
        )

    def test_tron_participate_asset(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                participate_asset_issue_contract=proto.TronParticipateAssetIssueContract(
                    to_address=bytes.fromhex(
                        "414F560EB4182CA53757F905609E226E96E8E1A80C"
                    ),
                    asset_name="CryptoChain",
                    amount=1,
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "0f752c52ee5daea6c740e0783398a03b1002a4a4e244ca0037981f18c0ad539b71b00bc1398297077373e303ddfe3fc48f7b8dc9afc4146bae5d7d448667d3c300"
        )

    def test_tron_account_update(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                account_update_contract=proto.TronAccountUpdateContract(
                    account_name="CryptoChainTest"
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "c4c1381d3a3e23010f19f8055df6d78990fdac619ae8be030425e0de0726f4fb665618a2c663c891cb5f8b26d009d79d3650008bda429e274bf4eee3330c806a00"
        )

    def test_tron_freeze_balance(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                freeze_balance_contract=proto.TronFreezeBalanceContract(
                    frozen_balance=10000000, frozen_duration=3
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "3c29d0e30913b37d997d9b40c664a8669653c2151702c449d01eeeaa8df65ce467970293daf0e1019e4efd94db9ca159cc65b9b04264d3e203f0abe5723a528d00"
        )

    def test_tron_unfreeze_balance(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                unfreeze_balance_contract=proto.TronUnfreezeBalanceContract()
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "20719064aa6d2ae4215fdd2c1818a8706f55d2d9fb9ae7bf482c7b5aae03c2f33213f7f1d7afbc8a4ed418bf21719d6ae2c0cc9f743139fea4374fdbc61ae48701"
        )

    def test_tron_withdraw_balance(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                withdraw_balance_contract=proto.TronWithdrawBalanceContract()
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "1b59288fa1086c2022eca7d34a63a9cb2adc8c3e72fd49602c6e048c5ab0a44d774f42b589021b0c9d582c6c861706b877336f5d6a114cbf5dbda0ff66cdf02900"
        )

    def test_tron_unfreeze_asset(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                unfreeze_asset_contract=proto.TronUnfreezeAssetContract()
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "2a5857885bb81ddb210f7a5fa1ae60e0acf9280b2bfb3a5c1463dee02e68ebce7486e11bf519c2cd6b42063ea6db919708ef9d2c8c0917636da4e7ea4518eda100"
        )

    def test_tron_update_asset(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                update_asset_contract=proto.TronUpdateAssetContract(
                    description="CryptoChain Token New Description",
                    url="http://cryptochain.network/token",
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "d6b39a251c5dbc0684672d4850c08eec9e5d1df2a9848e01d2b195e00962258651765bc314a5bd56b98aa91da70dfbbdc71526eef3cbf7c62878e541793bddba00"
        )

    def test_tron_proposal_create_contract(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                proposal_create_contract=proto.TronProposalCreateContract(
                    parameters=[
                        proto.TronProposalParameters(key=0, value=36000000),
                        proto.TronProposalParameters(key=6, value=300000000000),
                        proto.TronProposalParameters(key=4, value=5000000000),
                    ]
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "648d96f3a33ba90c5b3333c54d56fff2b81a70c80567aafe4eab092c1c1c09ff0b7724039a6f16a937f6bf1fa2dbb0c9843e1cbec63aeb8805141128b36d001301"
        )

    def test_tron_proposal_approve_contract(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                proposal_approve_contract=proto.TronProposalApproveContract(
                    proposal_id=10000, is_add_approval=False
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "a6cdfed4863d3f4d6adfba1444e47b277026d35d52988f223d2bed5eaa979c266ab74e7212df24f0f058661522bec05419ccfb28321c646632a8c502f06dda9e00"
        )

    def test_tron_proposal_delete_contract(self):
        load_device(self)

        msg = proto.TronSignTx(
            ref_block_bytes=bytes.fromhex("D0EF"),
            ref_block_hash=bytes.fromhex("6CD6025AFD991D7D"),
            expiration=1531429101000,
            timestamp=1531428803023,
            contract=proto.TronContract(
                proposal_delete_contract=proto.TronProposalApproveContract(
                    proposal_id=10000
                )
            ),
        )

        result = tron.sign_tx(self.client, parse_path(TRON_DEFAULT_PATH), msg)
        assert result.signature == unhexlify(
            "636577a6800c6ab4e7c11a72d5f0b3d865e190b51714cf5c4bd1d71bc37f54643582382314c236b489376bc4ab5d0612e3c6f9434e97db6dd41c517757cc8d7101"
        )
