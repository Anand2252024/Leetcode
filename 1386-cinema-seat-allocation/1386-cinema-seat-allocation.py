class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # All completely empty rows can fit 2 groups
        answer = (n - len(rows)) * 2

        for seats in rows.values():

            left = not any(seat in seats for seat in [2, 3, 4, 5])
            middle = not any(seat in seats for seat in [4, 5, 6, 7])
            right = not any(seat in seats for seat in [6, 7, 8, 9])

            if left and right:
                answer += 2
            elif left or middle or right:
                answer += 1

        return answer