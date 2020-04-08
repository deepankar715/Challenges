#!/bin/python

import binascii

def hex_to_base64(hex_str):
    return binascii.b2a_base64(binascii.a2b_hex(hex_str)).decode()

def main():
    hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    str_base64 = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

    print(hex_to_base64(hex_str))

if __name__ == '__main__':
    main()
