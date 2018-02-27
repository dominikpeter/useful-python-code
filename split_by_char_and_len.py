
import os
import re

s = 'Plattentrennmaschine VIP 260 230 V 0.65 kW Schnitttiefe 40 mm mit Diamanttrennscheibe 200 mm und Untergestell'

def split_by_char_and_length(s, m=20, pattern=" "):
    
    def split_by_char_and_length_rec(s, m=20, pattern=" ", l=[]):
        if len(s) < m:
            l.append(s)
            return l
        else:
            g = s[:m]
            r = g[::-1].find(" ")
            if r == -1:
                l.append(s[:m])
                return split_by_char_and_length_rec(s[m+len(pattern):], m=m, pattern=pattern, l=l)
            else:
                l.append(s[:m-r-len(pattern)])
                return split_by_char_and_length_rec(s[m-r:], m=m, pattern=pattern, l=l)
    l = []
    
    return split_by_char_and_length_rec(s=s, m=m, pattern=pattern, l=l)

" || ".join(split_by_char_and_length(s, m=40))

[len(i) for i in split_by_char_and_length(s, m=30)]
