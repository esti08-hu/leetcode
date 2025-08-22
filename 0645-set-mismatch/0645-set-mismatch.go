func findErrorNums(nums []int) []int {
    n := len(nums)
    numCount := make(map[int]int)
    for _, num := range nums {
        numCount[num]++
    }

    miss, dup := 0, 0
    for i := 1; i <= n; i++ {
        if count, ok := numCount[i]; !ok {
            miss = i
        } else if count > 1 {
            dup = i
        }
    }

    return []int{dup, miss}
}
