#!/usr/bin/env python3
#
# This file is part of the DecryptoCollection <https://github.com/ghettorce/decryptocollection>.
# Copyright (C) 2023 ultrayoba.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import sys
import argparse
from base64 import b64decode
from hashlib import sha256
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

HARD_SUFFIX = 'Eduard`s really cool string'


def build_encryption_key(timestamp, salt):
    return sha256((str(timestamp) + salt + HARD_SUFFIX).encode('UTF-8')).digest()


def decrypt(password, timestamp, salt, decode=True):
    key = build_encryption_key(timestamp, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv=b'\0' * 16)
    decrypted = cipher.decrypt(b64decode(password))
    decrypted = unpad(decrypted, cipher.block_size)
    if decode:
        decrypted = decrypted.decode('UTF-8')
    return decrypted


def parse_args():
    parser = argparse.ArgumentParser(description='TrueConf Server password decryptor')
    parser.add_argument('--raw', action='store_true', required=False,
                        help='Do not decode decrypted text')
    parser.add_argument('-u', '--username', type=str,
                        required=True, help='Salt value (user name)')
    parser.add_argument('cipher_text', type=str,
                        help='Encrypted value in the format "v2*timestamp*base64"')
    return parser.parse_args()


def main(args):
    try:
        _, timestamp, password = args.cipher_text.split('*')
    except:
        sys.exit('ERROR: unknown format')

    do_decode = not args.raw
    print(decrypt(password, timestamp, args.username.lower(), decode=do_decode))


if __name__ == '__main__':
    main(parse_args())
