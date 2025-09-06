func twoSum(numbers []int, target int) []int {
        l, r := 0, len(numbers)-1
        var curr_sum int 
        for l <= r{
            curr_sum = numbers[l] + numbers[r]
            if  curr_sum == target{
                return []int{l+1, r+1}
            } else {
                if curr_sum > target{
                    r-=1
                } else{
                    l+=1
                }
            }
        }
        return []int{-1}
}
