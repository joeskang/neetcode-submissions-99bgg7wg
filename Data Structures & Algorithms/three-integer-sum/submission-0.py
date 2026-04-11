class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort() # O(nlogn)

        for s in range(len(nums) - 2):
            m, e = s + 1, len(nums) - 1

            while m < e:

                if (sum_ := sum((nums[s], nums[m], nums[e]))) == 0:
                    answer.add((nums[s], nums[m], nums[e]))
                    m += 1
                    e -= 1
                elif sum_ < 0:
                    m += 1
                else:
                    e -= 1

        return list(answer)