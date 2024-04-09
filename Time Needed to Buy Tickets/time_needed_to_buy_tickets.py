from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        """
        Args:
            tickets: List[int] - tickets[i] denotes the number of tickets the ith customer will buy.
            k: int - The index of the customer whose time required to buy their tickets is being calculated.

        Returns:
            int - Time it takes for the kth customer to buy their tickets.
        """
        # naive approach: model customers being tickets and then enqueueing themselves

        head = 0  # customer at the start of the queue
        time = 0  # time elapsed
        while True:
            # find next customer
            while tickets[head] == 0:
                head = (head + 1) % len(tickets)

            # serve next customer
            time += 1  # incr time
            tickets[head] -= 1
            head = (head + 1) % len(tickets)

            # break when tickets[k] == 0 (kth customer has all of their tickets)
            if tickets[k] == 0:
                break

        return time
