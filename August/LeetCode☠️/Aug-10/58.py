class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        clean_text = s.rstrip()

        if " " in clean_text:
            rev = clean_text[::-1]
            return rev.index(" ")
        else:
            return len(clean_text)