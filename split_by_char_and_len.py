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

class Splitter(object):
    def __init__(self, string, length, pattern):
        self.string = string
        self.length = length
        self.pattern = pattern
        self.list = []
        self.combined = ''
        
    def to_list(self):
        self.list = split_by_char_and_length(self.string, self.length, self.pattern)
        return self.list
    
    def join(self, pattern):
        if not self.list:
            self.to_list()
        self.combined = pattern.join(self.list)
        return self.combined
