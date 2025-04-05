class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets = []
        def generate_subsets(index, subset):
            if index == len(nums):
                subsets.append(subset[:])
                return
            
            generate_subsets(index + 1, subset)
            subset.append(nums[index])
            generate_subsets(index + 1, subset)
        
        generate_subsets(0, [])
        
        out = 0
        for subset in subsets:
            temp = 0
            for num in subset:
                temp ^= num
            out += temp
        return out
