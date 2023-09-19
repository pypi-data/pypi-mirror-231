import unittest

from pyvalidator.is_ethereum_address import is_ethereum_address
from . import print_test_ok


class TestIsEthereumAddress(unittest.TestCase):

    def test_valid_ethereum_address(self):
        for i in [
            '0x0000000000000000000000000000000000000001',
            '0x683E07492fBDfDA84457C16546ac3f433BFaa128',
            '0x88dA6B6a8D3590e88E0FcadD5CEC56A7C9478319',
            '0x8a718a84ee7B1621E63E680371e0C03C417cCaF6',
            '0xFCb5AFB808b5679b4911230Aa41FfCD0cd335b42',
        ]:
            self.assertTrue(is_ethereum_address(i))
        print_test_ok()

    def test_invalid_ethereum_address(self):
        for i in [
            '0xGHIJK05pwm37asdf5555QWERZCXV2345AoEuIdHt',
            '0xFCb5AFB808b5679b4911230Aa41FfCD0cd335b422222',
            '0xFCb5AFB808b5679b4911230Aa41FfCD0cd33',
            '0b0110100001100101011011000110110001101111',
            '683E07492fBDfDA84457C16546ac3f433BFaa128',
            '1C6o5CDkLxjsVpnLSuqRs1UBFozXLEwYvU',
        ]:
            self.assertFalse(is_ethereum_address(i))
        print_test_ok()
