class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for r in image:
            r.reverse()
            for c in range(len(r)):
                r[c]^=1
        return image