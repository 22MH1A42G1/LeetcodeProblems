class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        l = len(encodedText)
        cols = l//rows
        ot = ''
        for i in range(cols):
            for j in range(i,l,cols+1):
                ot+=encodedText[j]
        return ot.rstrip()

