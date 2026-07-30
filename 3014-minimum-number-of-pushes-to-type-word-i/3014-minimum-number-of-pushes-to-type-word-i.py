class Solution:
    def minimumPushes(self, word: str) -> int:
        c = 0
        for i in range(len(word)):
            c+=math.floor(i/8)+1
        return c





        # l = len(word)
        # if l <= 8:
        #     return l
        # elif l >= 16:
        #     d = (l-8)*2
        #     return d+8+math.ceil(l/8)-2
        
        # else:
        #     d = (l-8)*2
        #     return d+8

