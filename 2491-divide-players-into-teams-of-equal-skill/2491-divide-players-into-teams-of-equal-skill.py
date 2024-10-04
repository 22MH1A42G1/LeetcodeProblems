class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistry, s = 0, skill[0] + skill[-1]

        for i in range(len(skill)//2):
            if skill[i] + skill[-i-1] == s:
                chemistry += skill[i] * skill[-i-1]
            else:
                return -1
        return chemistry