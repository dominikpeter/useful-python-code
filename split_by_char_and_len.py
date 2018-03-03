def split_by_char_and_len(s, m=20, pattern=" "):
    def split_by_char_and_len_rec(s, m=20, pattern=" ", l=[]):
        if len(s) < m: #piece is shorter than wished length
            l.append(s)
            return l
        else:
            g = s[:m]
            r = g[::-1].find(pattern)
            if r == -1:
                string_to_append = s[:m]
                assert(len(string_to_append) <= m)
                l.append(string_to_append)
                return split_by_char_and_len_rec(s[m+len(pattern):], m=m, pattern=pattern, l=l)
            else:
                string_to_append = s[:m-r-len(pattern)]
                assert(len(string_to_append) <= m)
                l.append(string_to_append)
                return split_by_char_and_len_rec(s[m-r:], m=m, pattern=pattern, l=l)
    l = []
    return split_by_char_and_len_rec(s=s, m=m, pattern=pattern, l=l)

class Splitter(object):
    def __init__(self, string, length, pattern):
        self.string = string
        self.length = length
        self.pattern = pattern
        self.list = []
        self.combined = ''
        
    def to_list(self):
        self.list = split_by_char_and_len(self.string, self.length, self.pattern)
        return self.list
    
    def join(self, pattern):
        if not self.list:
            self.to_list()
        self.combined = pattern.join(self.list)
        return self.combined
