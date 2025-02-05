// 128. Longest Consecutive Sequence
func longestConsecutive(nums []int) int {
    numsSet := make(map[int]struct{})
    for _, n := range nums {
        numsSet[n] = struct{}{}
    }
    maxLen := 0
    for n := range numsSet {
        if _, ok := numsSet[n-1]; !ok {
            length := 1
            for {
                if _, ok := numsSet[n+length]; ok {
                    length ++
                } else {
                    break
                }
            }
            maxLen = max(maxLen, length)
        }
    }
    return maxLen
}