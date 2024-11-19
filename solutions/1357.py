"""
    Question 1357: https://leetcode.com/problems/apply-discount-every-n-orders/

    Trivial question, just some array manipulation.
"""

class Cashier:
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.discount = discount

        self.product_id_to_price = {}
        for index in range(len(products)):
            self.product_id_to_price[products[index]] = prices[index]

        self.customer_index = 1

    def getBill(self, product: List[int], amount: List[int]) -> float:
        result = 0

        for index in range(len(product)):
            product_id = product[index]
            price = self.product_id_to_price[product_id]
            amount_purchased = amount[index]
            result = result + amount_purchased * price

        if self.customer_index % self.n == 0:
            result = result * (1 - self.discount * 0.01)
        
        self.customer_index = self.customer_index + 1

        return result

        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
