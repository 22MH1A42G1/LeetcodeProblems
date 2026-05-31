class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        for i in asteroids:
            if mass < i:
                return False
            mass+=i
        return True