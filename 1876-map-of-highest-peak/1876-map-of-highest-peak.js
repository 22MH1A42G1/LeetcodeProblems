/**
 * @param {number[][]} isWater
 * @return {number[][]}
 */
highestPeak = g => g.map(r => r.map(x => x ? 0 : 1e9)).reverse().map(r => g = r.reverse().map((x, j) => r = Math.min(x - 1, r, g[j] ?? 1e9) + 1, r = 1e9), g = []).reverse().map(r => g = r.reverse().map((x, j) => r = Math.min(x - 1, r, g[j] ?? 1e9) + 1, r = 1e9), g = [])
