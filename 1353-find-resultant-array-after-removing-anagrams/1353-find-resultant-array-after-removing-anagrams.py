class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(s1,s2):
            if len(s1)!=len(s2):
                return False
            return sorted(s1)==sorted(s2)
        i=1
        while i< len(words):
            if isAnagram(words[i-1],words[i]):
                words.pop(i)
            else:
                i+=1
        return words

        
        