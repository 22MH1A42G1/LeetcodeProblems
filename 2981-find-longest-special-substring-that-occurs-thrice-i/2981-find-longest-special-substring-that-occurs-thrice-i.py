class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)
        subs = [''.join(sub) for _, sub in groupby(s)] 
        for i in subs:                                 
            d[i]+= 1                                   
            if len(i) > 1: d[i[1:]]+= 2              
            if len(i) > 2: d[i[2:]]+= 3              
        return max(map(len,filter(lambda x: d[x] > 2,d)), default = -1)