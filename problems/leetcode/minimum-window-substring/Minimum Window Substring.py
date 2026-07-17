class Solution:
    def minWindow(self, s, t):
        target, mem, initial = {}, {}, set()
        for c in t:
            target[c] = target.get(c, 0) + 1
            initial.add(c)
        
        size = 0
        for i in range(len(s)):
            c = s[size]
            if c in target:
                mem[c] = mem.get(c, 0) + 1
                if mem[c] == target[c]:
                    initial.discard(c)
            if not initial:
                break
            size += 1
        if initial:
            return ""

        ans = (0, size+1)
        i = 0
        while True:
            if self.contained(mem, target):
                while True:
                    c = s[i]
                    if c not in mem:
                        pass
                    elif mem[c] > target[c]:
                        mem[c] -= 1
                    else:
                        break
                    
                    size -= 1
                    i += 1
                ans = (i, i+size+1)
            i += 1
            if i+size >= len(s):
                break
            if s[i-1] in mem:
                mem[s[i-1]] -= 1
            if s[i+size] in mem:
                mem[s[i+size]] += 1

        return s[ans[0]: ans[1]]
    
    def contained(self, window, target):
        for k in window:
            if window[k] < target[k]:
                return False
        return True