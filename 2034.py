# Question 2034: https://leetcode.com/problems/stock-price-fluctuation/

"""
    Always when a questions asks for the maximum and minimum of a stream, I suspect I have to use a heap.
"""

class StockPrice:
    def __init__(self):
        self.dict_hash = {}
        self.min_heap = []
        self.max_heap = []
        self.current_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.dict_hash[timestamp] = price

        heapq.heappush(self.min_heap, (price, timestamp))
        heapq.heappush(self.max_heap, (-1*price, timestamp))
        heapq.heappush(self.current_heap, -1*timestamp)

    def current(self) -> int:
        el = self.current_heap[0]
        timestamp = (-1) * el
        
        return self.dict_hash[timestamp]

    def maximum(self) -> int:
        while True:
            el = self.max_heap[0]
            
            price = -1*el[0]
            timestamp = el[1]
            
            if self.dict_hash[timestamp] == price:
                return price
            
            heapq.heappop(self.max_heap)
        

    def minimum(self) -> int:
        while True:
            el = self.min_heap[0]
            
            price = el[0]
            timestamp = el[1]
            
            if self.dict_hash[timestamp] == price:
                return price
        
            heapq.heappop(self.min_heap)

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()