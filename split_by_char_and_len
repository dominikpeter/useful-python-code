import os
import re

s = 'das ist ein test zum splitten von text'

def isplit(s, m=10, pattern=" ", i=0):
    if i + s.find(pattern) > m:
        return i - len(pattern)
    else:
        c = s.find(pattern) + len(pattern)
        i += c
        return isplit(s[c:], m=m, pattern=pattern, i=i)
        
        
def tsplit(s, l=[], m=10, pattern=" "):
    if len(s) > m:
        idx = isplit(s, m=m, pattern=pattern)
        t = s[:idx]
        l.append(t)
        return tsplit(s[idx+1:], l, m=m)
    else:
        l.append(s)
        return l
        
        
def split_by_char_and_length(s, m=10, pattern=" "):
    l = []
    l = tsplit(s, l=l, m=m, pattern=pattern)
    return l
    
" / ".join(split_by_char_and_length(s, m=10, pattern=" "))

