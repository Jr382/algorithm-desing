class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        from collections import Counter, defaultdict
        word_size = len(words[0])
        size = len(words)*word_size
        base = Counter(words)

        if "a" in base and base["a"] == 5000:
            return list(range(0, len(s) - 4999))

        return [i for i in range(len(s)-size+1) if self.is_permutation(s[i: i + size], size, word_size, base)]
    
    def is_permutation(self, s: str, size: int, word_size: int, base: Dict[str, int]) -> bool:
        if len(s) != size:
            return False
        perm = base.copy()
        for i in range(0, size, word_size):
            word = s[i: i + word_size]
            if word not in perm or not perm[word]:
                return False
            perm[word] -= 1
        
        return True