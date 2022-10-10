class Solution:
    num=0
    def romanToInt(self, s: str) -> int:
        if(len(s) == 0):
            return self.num
        if s[0]=='I':
            if len(s) > 1:
                if s[1]=='V':
                    self.num+=4
                    return self.romanToInt(s[2:])
                elif s[1]=='X':
                    self.num+=9
                    return self.romanToInt(s[2:])
                else:
                    self.num+=1
                    return self.romanToInt(s[1:])
            else:
                self.num+=1
                return self.romanToInt(s[1:])
        elif s[0]=='V':
            self.num+=5
            return self.romanToInt(s[1:])
        elif s[0]=='X':
            if len(s)>1:
                if s[1]=='L':
                    self.num+=40
                    return self.romanToInt(s[2:])
                elif s[1]=='C':
                    self.num+=90
                    return self.romanToInt(s[2:])
                else:
                    self.num+=10
                    return self.romanToInt(s[1:])
            else:
                self.num+=10
                return self.romanToInt(s[1:])
        elif s[0]=='L':
            self.num+=50
            return self.romanToInt(s[1:])
        elif s[0]=='C':
            if len(s)>1:
                if s[1]=='D':
                    self.num+=400
                    return self.romanToInt(s[2:])
                elif s[1]=='M':
                    self.num+=900
                    return self.romanToInt(s[2:])
                else:
                    self.num+=100
                    return self.romanToInt(s[1:])
            else:
                self.num+=100
                return self.romanToInt(s[1:])
        elif s[0]=='M':
            self.num+=1000
            return self.romanToInt(s[1:])
        else:
            self.num+=500
            return self.romanToInt(s[1:])