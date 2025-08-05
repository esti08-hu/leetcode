func applyOperations(nums []int) []int {
	n := len(nums)
	for i := 0; i < n-1; i++ {
		if nums[i] == nums[i+1] && nums[i] != 0 {
			nums[i] *= 2
			nums[i+1] = 0
		}
	}

	j := 0
	for i := 0; i < n; i++ {
		if nums[i] != 0 {
			nums[j] = nums[i]
			j++
		}
	}

	for j < n {
		nums[j] = 0
		j++
	}

	return nums
}