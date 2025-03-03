class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U',}
        temp = list(s)

        start = 0
        end = len(s) - 1

        while start < end:
            if temp[start] in vowels and temp[end] in vowels:
                temp[start], temp[end] = temp[end], temp[start]
                start += 1
                end -= 1

            elif temp[start] in vowels:
                end -= 1

            elif temp[end] in vowels:
                start += 1

            else:
                start += 1
                end -= 1

        return "".join(temp)
    
if __name__ == "__main__":
    solution = Solution()

    s = "IceCreAm"
    #s = "leetcode"

    print(solution.reverseVowels(s))