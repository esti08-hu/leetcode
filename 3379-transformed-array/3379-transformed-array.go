func constructTransformedArray(nums []int) []int {
	result := make([]int, len(nums))
	for i, v := range nums {
		if v > 0 {
			steps := (i + v) % len(nums)
			result[i] = nums[steps]
		} else if v < 0 {
			steps := ((i + v) % len(nums) + len(nums)) % len(nums)
			result[i] = nums[steps]
		} else {
			result[i] = v
		}
	}
	return result
}