"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers
cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return if n new flowers can be planted in the flowerbed without violating the
no-adjacent-flowers rule.
"""

from math import floor
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """Determines if `n` flowers can be planted in `flowerbed`

        #### Arguments
            `flowerbed: List[int]` list of 0s and 1s, where 0 means an empty plot and 1 means a
            flower is already planted there
            `n: int` the number of flowers to plot

        #### Returns
            `bool` `True` if we can plot `n` flowers, otherwise `False`

        ---
        This solution transforms `flowerbed` through a series of 8 steps that calculate the maximum

        number of flowers that can be plotted in `flowerbed`. After the maximum is calculated, we

        simply return if `n` is less than or equal to it.

        Those 8 steps are:
        1. Pad `flowerbed` with a 0 on each side (see footnote for reasoning).

        ```py
        [0] -> [0, 0, 0]
        ```

        2. Cast each integer to a string.

        ```py
        [0, 1, 0, 0, 1, 0] -> ["0", "1", "0", "0", "1", "0"]
        ```

        3. Concatenate the strings of `flowerbed` together.

        ```py
        ["0", "1", "0", "0"] -> "0100"
        ```

        4. Split `flowerbed` by `"1"`.

        ```py
        "010010" -> ["0", "", "00", "", "0]
        ```

        5. Filter empty strings out of `flowerbed`.

        ```py
        ["0", "", "0"] -> ["0", "0"]
        ```

        6. Map each string of zeros to its length.

        ```py
        ["0", "00", "0"] -> [1, 2, 1]
        ```

        7. Map each length to the maximum number of flowers that can be plotted where:

        ```py
        from math import floor
        max_flowers = floor((length - 1) / 2)
        ```

        ```py
        [2, 8, 3, 7, 3] -> [0, 3, 1, 3, 1]
        ```

        8. Sum each number together

        ```py
        [0, 3, 1, 3, 1] -> 8
        ```

        ---
        #### Footnote

        We pad each side by a 0, so the formula at step 7 works with empty spots that are at the

        beginning or ending of `flowerbed`.

        Imagine if we wanted to plant one flower and `flowerbed` looked like this:

        ```py
        flowerbed = [0, 0, 1]
        ```

        We can plant a flower at `flowerbed[0]`, but step 7 would only see the two zeros at

        `flowerbed[0:2]` and conclude that no flowers can be planted there. We can solve this by

        padding an imaginary flower at the boundaries, so that we're allowed to plant flowers at the

        first and last indices.
        """
        return n <= sum(  # step 8
            map(
                lambda n: floor((n - 1) / 2),  # step 7
                map(
                    lambda s: len(s),  # step 6
                    filter(
                        lambda s: s != "",  # step 5
                        "".join(  # step 3
                            map(
                                lambda flower: str(flower),  # step 2
                                [0, *flowerbed, 0],  # step 1
                            )
                        ).split("1"),  # step 4
                    ),
                ),
            )
        )
