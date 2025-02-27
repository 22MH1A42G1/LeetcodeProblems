from itertools import combinations
class Solution:
	def lenLongestFibSubseq(self, A: list[int]) -> int:
		s, m = set(A), {}
		for b, c in combinations(A, 2):
			if (a := c - b) < b and a in s:
				m[b, c] = m.get((a, b), 2) + 1 
		return max(m.values(), default=0)