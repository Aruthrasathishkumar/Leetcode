def split_array(nums):
    left, right = 0, len(nums) - 1
    left_sum = nums[left]
    right_sum = nums[right]

    while left < right - 1:
        if left_sum < right_sum:
            left += 1
            left_sum += nums[left]
        else:
            right -= 1
            right_sum += nums[right]

    if left_sum == right_sum:
        return right  # right part starts here
    return -1

