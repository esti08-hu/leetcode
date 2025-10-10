func numSquares(n int) int {
    cache := make(map[[1]int]int)

    var dp func(x int) int

    dp = func(x int) int {
        if x == 0 {
            return 0
        }
        if x >= 1 && x <= 3 {
            return x
        }

        if val, ok := cache[[1]int{x}]; ok {
            return val
        }

        min_sqr := int(math.Sqrt(float64(x)))
        curr := n+1


        for i:=min_sqr; i > 0; i-- {
            if x >= i*i {
                curr = min(curr, 1+dp(x-i*i))

            }
        }
        cache[[1]int{x}]=curr
        return cache[[1]int{x}]
    }
    return dp(n)

}