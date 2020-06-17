" Bulls and Cows "

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic1 = collections.Counter(secret)
        dic2 = collections.Counter(guess)

        bulls, cows = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                key=secret[i]
                bulls += 1
                dic1[key] -= 1
                dic2[key] -= 1
        for key in dic1:
            if key in dic2:
                cows += min(dic1[key], dic2[key])
        return  str(bulls) + "A" + str(cows) + "B"
