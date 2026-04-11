class Solution:
    def maxArea(self, heights: List[int]) -> int:
        answer = -float(math.inf)

        s, e = 0, len(heights) - 1

        while s < e:
            answer = max(answer, (min(heights[s], heights[e]) * (e - s)))
            if heights[s] < heights[e]:
                s += 1
            else:
                e -= 1

        return answer

        