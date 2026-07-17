class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == ".*" or (not p and not s):
            return True

        if not p: 
            return False

        if len(p) > 1 and p[1] == "*":
            i = 0
            while i < len(s) and (p[0] == s[i] or p[0] == "."):
                if self.isMatch(s[i:], p[2:]):
                    return True
                i += 1
        
            return self.isMatch(s[i:], p[2:])
        

        return (len(s) > 0 and (p[0] == "." or s[0] == p[0])) and self.isMatch(s[1:], p[1:])


            

                
                