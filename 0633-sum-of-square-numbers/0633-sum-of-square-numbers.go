func judgeSquareSum(c int) bool {
    sr := int(math.Sqrt(float64(c)))
    l, r := 0, sr

    for l <= r{
        curr := l*l + r*r
        if curr > c {
            r-- 
        }else if curr < c {
            l++
        }else {
            return true
        }
    }
    return false
}

