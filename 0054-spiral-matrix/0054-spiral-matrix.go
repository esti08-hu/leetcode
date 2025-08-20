func spiralOrder(matrix [][]int) []int {
    res := []int{}

        t, b := 0, len(matrix) - 1
        l, r := 0, len(matrix[0]) - 1
    if len(matrix) == 0 || len(matrix[0]) == 0 {
        return res 
    }

    for t <= b && l <= r{
        for i:=l; i < r+1; i++ {
            res = append(res, matrix[t][i])
        }
        t+=1

        for i:=t; i < b+1; i++ {
            res = append(res, matrix[i][r])
        }
        r-=1
            
        if t <= b {
            for i:=r; i > l -1; i-- {
                res = append(res, matrix[b][i])
            }
        }
        b-=1

        if l <= r {
            for i:=b; i > t- 1; i-- {
                res = append(res, matrix[i][l])
            }
        }
        l += 1
            
    }
    return res
}