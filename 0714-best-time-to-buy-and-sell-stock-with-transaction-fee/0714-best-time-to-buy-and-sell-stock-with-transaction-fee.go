func maxProfit(prices []int, fee int) int {
    cache := make(map[[2]int]int)
    var dfs func(i int, state int) int

    dfs = func (i int, state int) int{
        if i >= len(prices){
            return 0
        }

        if val, ok:= cache[[2]int{i, state}]; ok {
            return val
        }

        if state == 0{
            buy := dfs(i+1, 1)-prices[i]
            skip := dfs(i+1, 0)
            cache[[2]int{i, state}] = max(buy, skip)
        } else if state == 1{
            sell := dfs(i+1, 0)+prices[i] - free
            skip := dfs(i+1, 1)
            cache[[2]int{i, state}] = max(sell, skip)
        }

        return cache[[2]int{i, state}]
    }
    return dfs(0,0)
    
}