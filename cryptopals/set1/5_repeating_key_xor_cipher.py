#!/bin/python

import binascii

def encrypt(plain_text, key):
    plain_text = binascii.a2b_qp(plain_text)
    key = binascii.a2b_qp(key)
    cipher_arr = []
    for i in range(len(plain_text)):
        cipher_arr.append(binascii.hexlify(bytes([plain_text[i] ^ key[i%len(key)]])))
    return b"".join(cipher_arr).decode()

def main():
    plain_text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    given_result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"
    print(encrypt(plain_text, "ICE") == given_result)

if __name__ == '__main__':
    main()
