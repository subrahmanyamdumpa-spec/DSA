class Solution:
    def subarraysDivByK(self, nums, k):
        remainder_count = {0: 1}
        prefix = 0
        answer = 0

        for num in nums:
            prefix += num
            remainder = prefix % k

            if remainder in remainder_count:
                answer += remainder_count[remainder]

            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return answer        