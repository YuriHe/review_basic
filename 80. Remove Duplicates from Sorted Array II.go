func removeDuplicates(nums []int) int {
    k, count := 1, 1
    for i := 1; i < len(nums); i++ {
        if nums[i] != nums[i-1] {
            nums[k] = nums[i]
            k += 1
            count = 1
        } else {
            if count < 2 {
                nums[k] = nums[i]
                k += 1
                count += 1
            }
        }
    }
    return k
}