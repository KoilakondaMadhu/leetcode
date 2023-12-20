from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Assume the Minimum Cost to be Infinity
        min_cost = float('inf')

        # Number of Chocolates
        n = len(prices)

        # Check Each Chocolate Price
        for choco_price in prices:
            # Update the Minimum Cost
            min_cost = min(min_cost, choco_price)

        # We can buy chocolates only if we have enough money
        if min_cost <= money:
            # Return the Amount of Money Left
            return money - min_cost
        else:
            # We cannot buy chocolates. Return the initial amount of money
            return money
