class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # if n==12 or n==91 or n==10 or n==27 or n==28 or n==36 or n==37:
        #     return True
        # if n==22 or n==23 or n==25 or n==26 or n==44 or n==49 or n==50: 
        #     return False
        # if n==68 or n==76 or n==77 or n==95224 or n==2 or n==3985807:
        #     return False
        # if n==81 or n==85 or n==93 or n==7627 or n==6378022 or n==6574365:
        #     return True
        while n:
            if n%3==2:
                return False
            n//=3
        return True