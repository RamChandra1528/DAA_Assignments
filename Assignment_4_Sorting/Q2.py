class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = [None] * len(words)
        
        for word in words:
            position = int(word[-1]) - 1
            sorted_words[position] = word[:-1]
        
        return ' '.join(sorted_words)

s = Solution()
t=s.sortSentence("is2 sentence4 This1 a3")
print(t)