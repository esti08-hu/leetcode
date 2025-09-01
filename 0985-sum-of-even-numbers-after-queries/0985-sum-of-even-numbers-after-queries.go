func sumEvenAfterQueries(nums []int, queries [][]int) []int {
		res := make([]int, len(queries))
		sum := 0
		for _, num := range nums {
			if num%2 == 0 {
				sum += num
			}
		}
		for i, q := range queries {
			val, idx := q[0], q[1]
			if nums[idx]%2 == 0 {
				sum -= nums[idx]
			}
			nums[idx] += val
			if nums[idx]%2 == 0 {
				sum += nums[idx]
			}
			res[i] = sum
		}
		return res
}