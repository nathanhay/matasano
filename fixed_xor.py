#!/usr/bin/env python

def fixed_xor(s1, s2):
  """Returns the value of string s1 (or its length up to the length of s2) XOR'd w/ string s2, 
  converting s1 and s2 to hexadecimal form via int()."""
    if len(s1) > len(s2):
        return '%x' % (int(s1[:len(s2)],16)^int(s2,16))
    else:
        return '%x' % (int(s1,16)^int(s2[:len(s1)],16))

x = '1c0111001f010100061a024b53535009181c'
y = '686974207468652062756c6c277320657965'

print(fixed_xor(x,y))
