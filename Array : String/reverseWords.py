class Solution:
    def reverseWords(self, s: str) -> str:
        
        temp = s.split()
        #print(temp)
        size = len(temp)

        tempReversed = []

        for item in temp:
            tempReversed.append(temp[size - 1])
            size -= 1

            a = (" ".join(tempReversed))
        return a
    
if __name__ == "__main__":
    solution = Solution()

    s = "the sky is blue"
    print(solution.reverseWords(s))