#!/bin/python

import binascii

def single_byte_xor(hex_str):
    bin_str = binascii.a2b_hex(hex_str)
    clear_txt = [[] for x in range(256)]
    key_value = {}

    for key in range(256):
        tmp = b''
        for byt in bin_str:
            tmp += bytes([byt ^ key])
        clear_txt[key].append(tmp.decode('utf-8', 'ignore'))
        key_value[str(chr(key))] = clear_txt[key]
    return(key_value)

def str_freq(str):
    weights = {"a": .08167,    "b": .01492,    "c": .02202,    "d": .04253,
               "e": .12702,    "f": .02228,    "g": .02015,    "h": .06094,
               "i": .06966,    "j": .00153,    "k": .01292,    "l": .04025,
               "m": .02406,    "n": .06749,    "o": .07507,    "p": .01929,
               "q": .00095,    "r": .05987,    "s": .06327,    "t": .09356,
               "u": .02758,    "v": .00978,    "w": .02560,    "x": .00150,
               "y": .01994,    "z": .00077}
    score = 0
    for let in str.lower():
        try:
            score += weights[let]
        except KeyError:
            score += 0
    return score

def decrypt(key_value, score_bound):
    key_score = {}
    for key in key_value:
        key_score[key] = str_freq("".join(key_value[key]))
    sorted_scores = {k: v for (k, v) in sorted(key_score.items(), key=lambda item: item[1], reverse=True) if v>score_bound}

    return sorted_scores

def main():
    hex_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    key_value = single_byte_xor(hex_str)
    sorted_scores = decrypt(key_value, 1)
    for key in sorted_scores.keys():
       print(f"Possible key = {key}\nscore = {sorted_scores[key]}\nplain text = {''.join(key_value[key])}\n--------\n")



if __name__ == '__main__':
    main()
