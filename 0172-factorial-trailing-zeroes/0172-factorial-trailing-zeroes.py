class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(1000000)

        n = str(math.factorial(n))

        count = 0
        if n[-1]=="0":
            for i in range(len(n)-1, -1, -1):
                if n[i] == "0":
                    count+=1
                else:
                    break
        return count