#!/bin/python

import binascii

def fixed_xor(str1, str2):
    bin1 = binascii.a2b_hex(str1)
    bin2 = binascii.a2b_hex(str2)

    if len(bin1) == len(bin2):
        return binascii.b2a_hex(bytes(a ^ b for a, b in zip(bin1, bin2))).decode().strip()
    else:
        print("Not equal")
        return None

def main():
    num1 = "1c0111001f010100061a024b53535009181c"
    num2 = "686974207468652062756c6c277320657965"

    print(fixed_xor(num1, num2))
    print("746865206b696420646f6e277420706c6179")
    print("equal?")

if __name__ == '__main__':
    main()
