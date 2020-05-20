class StockSpanner:

    def __init__(self):
        self.numbers = []

    def next(self, price: int) -> int:
        
        count = 1
        while self.numbers and self.numbers[-1][0] <= price: 
            count += self.numbers.pop()[1]
        
        self.numbers.append((price, count))
        return self.numbers[-1][1]
            
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)