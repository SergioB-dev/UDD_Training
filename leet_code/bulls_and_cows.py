class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        letter_list = []
        bull_positions = {}
        cows = 0
        bulls = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:  # We have a match at matching positions - Bull
                bull_positions[i] = guess[i]
                bulls += 1
            else:
                letter_list.append(secret[i])
        
        for i in range(len(secret)):
            if i in bull_positions:
                continue
            elif guess[i] in letter_list:
                cows += 1
                letter_list.remove(guess[i])
   
        return f"{bulls}A{cows}B"
