# DecryptoCollection
[![Twitter](https://img.shields.io/twitter/url?label=Tweet%20to%20%40ultrayoba&style=social&url=https%3A%2F%2Ftwitter.com%2Fintent%2Ftweet%3Fscreen_name%3Dultrayoba)](https://twitter.com/intent/tweet?screen_name=ultrayoba)

A personal collection of scripts for decrypting various things (mainly from proprietary software).

Useful during penetration testing/red team operations for obtaining credentials for lateral movement.

# Contents
[PRTG Network Manager](#prtg-network-manager)

## [PRTG Network Manager](prtg)
Decryptor for encrypted strings such as `windowsloginpassword` from the `PRTG Configuration.dat` file.

### Configuration Location
`C:\ProgramData\Paessler\PRTG Network Monitor\` *(default)*

### Download
```sh
wget https://raw.githubusercontent.com/ghettorce/decryptocollection/main/prtg/prtg_string_decryptor.py
```

### Usage
```
usage: prtg_string_decryptor.py [-h] [--raw] {bf1,bf2,aes} ... cipher_text

PRTG string decryptor.

positional arguments:
  {bf1,bf2,aes}
    bf1          LockBox 2 Blowfish with Base64 encoding.
    bf2          LockBox 3 Blowfish with custom Base64 alphabet.
    aes          OpenSSL AES256 with Base32 encoding.
  cipher_text    Encoded cipher text (Base32 / Base64).

optional arguments:
  -h, --help     show this help message and exit
  --raw          Do not decode decrypted text.
```

### Examples
Cipher **bf1** - found in **9.\*** and earlier:
```sh
> prtg_string_decryptor.py bf1 'a4wqOlR4V9Yf6VlOJBkkpQ=='
testpass
```
Cipher **bf2** - found in **13.\***, **15.\***:
```sh
> prtg_string_decryptor.py bf2 '/P5N0Gm32nmpimNshgxE9tpuBVeBYG7P'
testpass
```
Cipher **aes** - found in **22.\*** and earlier *(latest algo)*:
```sh
> prtg_string_decryptor.py aes --guid '{94B4CDA1-5BFC-48C9-992C-8EFB0965CACF}' '5VKX3XJFPSQWPS3NJDJHFUV5PQN54TIURCGP5UI='
testpass
```
*The **guid** value is stored in the attribute of **root** node in `PRTG Configuration.dat` file*.