class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        time: O(n)
        space: O(n)
        """
        n = len(nums)
        stack, res = [], [-1] * n
        for i in range(n * 2):
            idx = i % n
            while stack and (nums[stack[-1]] < nums[idx]):
                res[stack.pop()] = nums[idx]
            if res[idx] == -1:
                stack.append(idx)
        return res

    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        time: O(n)
        space: O(n)
        """
        st = [0]
        ans = [0] * len(temp)
        for i in range(1, len(temp)):
            while st and temp[st[-1]] < temp[i]:
                ans[st[-1]] = i - st[-1]
                st.pop()
            st.append(i)
        return ans