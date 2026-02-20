def split_array(nums):
    total = sum(nums)
    left_sum = 0

    # i is the last index of the left part
    for i in range(len(nums) - 1):
        left_sum += nums[i]
        right_sum = total - left_sum

        if left_sum == right_sum:
            return i + 1  # right part starts here

    return -1
