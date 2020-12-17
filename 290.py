class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        length = len(pattern)
        s = s.split()
        if len(s) != length:
            return False
        d1 = {}
        d2 = {}
        fl = 1
        for i in range(length):
            pp = pattern[i]
            ss = s[i]
            if pp in d1:
                if d1[pp] != ss:
                    fl = 0
                    break
            else:
                d1[pp] = ss
            if ss in d2:
                if d2[ss] != pp:
                    fl = 0
                    break
            else:
                d2[ss] = pp
        if fl:
            return True
        else:
            return False