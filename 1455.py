" Check If a Word Occurs As a Prefix of Any Word in a Sentence "

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        li=sentence.split()
        for x in range(len(li)):
            word = li[x]
            i, j = 0, len(word) - 1
            m, n = 0, len(searchWord) - 1
            while i <= j and m <= n:

                if word[i] == searchWord[m]:
                    i+= 1
                    m+=1
                    if i == len(searchWord) :
                        return x + 1
                else:
                    break

        return -1
