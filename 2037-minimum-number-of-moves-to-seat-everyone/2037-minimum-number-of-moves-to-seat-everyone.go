func AbsoluteValue(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
func minMovesToSeat(seats []int, students []int) int {
    sort.Ints(seats)
    sort.Ints(students)
    n := len(students)
    res := 0
    for i:=0; i < n; i++ {
        res += AbsoluteValue(students[i]-seats[i])
    }

    return res
    
}