class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3:
            return False

        target = total // 3
        acc = 0
        parts = 0
        for i in range(len(arr) - 1):
            acc += arr[i]
            if acc == target:
                parts += 1
                acc = 0
                if parts == 2:
                    return True

        return False
