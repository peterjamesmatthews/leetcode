from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        if len(students) != len(sandwiches):
            raise ValueError(
                f"number of students and sandwiches are not equal: {len(students)} != {len(sandwiches)}"
            )

        i_front = 0
        misses = 0
        while len(students) > 0:
            if students[i_front] == sandwiches[0]:
                del students[i_front]
                del sandwiches[0]
                i_front = i_front % len(students) if len(students) > 0 else 0

                misses = 0
            else:
                i_front = (i_front + 1) % len(students)

                misses += 1
                if misses == len(students):
                    break

        return len(students)
