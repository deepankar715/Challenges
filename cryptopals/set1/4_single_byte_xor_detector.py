#!/bin/python

import binascii
import single_byte_xor_cipher as sbxc

def main():
    with open("4.txt", "r") as file:
        hex_arr = file.read().split("\n")

        key_value_arr = []
        for hex in hex_arr:
            key_value_arr.append(sbxc.single_byte_xor(hex))

        sorted_scores_arr = []
        for key_value in key_value_arr:
            sorted_scores_arr.append(sbxc.decrypt(key_value, 1.3))

        count = 0
        for index in range(len(hex_arr)):
            for key in sorted_scores_arr[index].keys():
                print(f"hex = {hex_arr[index]}\nhex index = {index}\npossible key = {key}\nscore = {sorted_scores_arr[index][key]}\nplain text = {''.join(key_value_arr[index][key])}\n--------\n")
                count += 1

        print(f"Number of results: {count}")
    # answer is on hex of line number 170, with key = '5' and score ~ 1.4

if __name__ == '__main__':
    main()
