import functools
from typing import List, Tuple, TypedDict


class EvensOdds(TypedDict):
    evens: int
    odds: int


class Solution:
    @staticmethod
    def f(evens_odds: EvensOdds, i_bit: Tuple[int, str], offset: int = 0) -> EvensOdds:
        i, bit = i_bit

        if bit == "1":
            if (i + offset) % 2 == 0:  # even
                evens_odds["evens"] += 1
            else:  # odd
                evens_odds["odds"] += 1

        return evens_odds

    def evenOddBit(self, n: int) -> List[int]:
        bits = bin(n)[2:]  # str binary representation of n w/out prefixed "0b"
        enum_bits = enumerate(bits)  # iter for index and value of bits

        # enumerate and bits have reversed indexing, so correct this with an offset
        g = functools.partial(Solution.f, offset=len(bits) - 1)

        # count the number of "1"s in even and odd indices
        evens_odds = functools.reduce(g, enum_bits, {"evens": 0, "odds": 0})

        return [evens_odds["evens"], evens_odds["odds"]]
