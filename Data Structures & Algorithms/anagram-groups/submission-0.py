class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n mlogm) 
        base_dict = defaultdict(list)
    
        for string in strs:
            sorted_string = ''.join(char for char in sorted([_ for _ in string]))
            base_dict[sorted_string].append(string)

        return list(base_dict.values())

        

