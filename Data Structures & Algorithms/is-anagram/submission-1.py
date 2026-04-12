class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter, t_counter = Counter(s), Counter(t)

        for s_key, s_val in s_counter.items():
            if s_key not in t_counter or s_val != t_counter[s_key]:
                return False

        for t_key, t_val in t_counter.items():
            if t_key not in s_counter or t_val != s_counter[t_key]:
                return False

        return True