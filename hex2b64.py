#!/usr/bin/env python
# Nathan Hay, Matasano crypto challenge 1, 2015.11.03
import base64

test = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
def hex2base64(s):
    return base64.b64encode(s.decode("hex"))

print(hex2base64(test))
