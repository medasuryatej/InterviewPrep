class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right, ans, curr_sum, data_set, end = 0,0,0,0,set(),len(nums)
        while right < end:
            if nums[right] not in data_set:
                curr_sum += nums[right]
                data_set.add(nums[right])
                # increase right side limit of sliding window by 1
                #[left,right)
                right += 1
                ans = max(curr_sum, ans)
            else:
                # when duplicate element already encountered
                # try to move left index by 1
                # since you have already kept track of sum till the current right index
                # elements from left(beg) no longer needed
                curr_sum -= nums[left]
                data_set.remove(nums[left])
                left += 1
        return ans