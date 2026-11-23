class ProductOfNumbers:

    def __init__(self):
        self.List = [1]

    def add(self, num: int) -> None:
        if num==0:
            self.List = [1]
        else:
            self.List.append(self.List[-1]*num)
    def getProduct(self, k: int) -> int:
        n = len(self.List)
        return 0 if k>=n else self.List[-1]//self.List[n-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)