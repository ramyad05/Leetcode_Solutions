class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        mid  = len(s) // 2
        a = sum(ch in vowels for ch in s[:mid])
        b = sum(ch in vowels for ch in s[mid:])
        return a == b
        