#!/usr/bin/env python3

import string
import unittest
import prtg_string_decryptor


class TestPaeDecryptors(unittest.TestCase):
    def setUp(self):
        self.plain_text = string.ascii_letters + string.digits
        self.cipher_text_bf1_b64 = (
            'fos6KkF/Q812gzIiSXdL1W6bKjpRb1PdZpMYDGddYeNYoRAEb1Vp61C5CBx3TXHzS'
            'LEAFBQoFpYr3G95HCAkow=='
        )
        self.cipher_text_bf2_b64 = (
            'wUAuKnxOrdNeoijDTwR1wi0iYY3zpQD0CHq48qZ/AxiSYhHnp/cbvy5KfNoGD2lsj'
            'JE0MB1CRDeDirIIDbHshRtuwQSeewqK22fuojqhJqS0G28pvqGdVw6es4kjvK1i8U'
            'SCxWuVA5ZU6fW/wQQbdUQxZTrx5bb9XCf04yaJcUs='
        )
        self.cipher_text_aes_b32 = (
            '7RFYN5AON365X2RTNMW5AWQGAF5HXC4EPG5WJAN35AS2DRMFABFE3UMG3D5PQMPTW'
            '7YP7JMG32HQLV3MSUCFZNWPM6NCHUAGLWYDTYBSI4DA6DWBNMU2DAQIEFAI6==='
        )
        self.guid_aes = '{94B4CDA1-5BFC-48C9-992C-8EFB0965CACF}'

    def test_bf1(self):
        cipher = prtg_string_decryptor.PaeCipherBlowfishV1()
        self.assertEqual(cipher.decrypt(self.cipher_text_bf1_b64), self.plain_text)

    def test_bf2(self):
        cipher = prtg_string_decryptor.PaeCipherBlowfishV2()
        self.assertEqual(cipher.decrypt(self.cipher_text_bf2_b64), self.plain_text)

    def test_aes(self):
        cipher = prtg_string_decryptor.PaeCipherAES256(guid=self.guid_aes)
        self.assertEqual(cipher.decrypt(self.cipher_text_aes_b32), self.plain_text)


if __name__ == '__main__':
    unittest.main()
