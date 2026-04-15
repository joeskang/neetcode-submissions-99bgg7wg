class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ''
        index = 0
        while 1:
            current_char = None

            for string in strs:
                if index > len(string) - 1:
                    return answer

                if not current_char:
                    current_char = string[index]
                    continue

                if current_char != string[index]:
                    return answer

            answer += current_char
            index += 1
