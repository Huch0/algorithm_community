class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            # Base case : Reach the end of the combination tree
            if len(digits) == len(path):
                combinations.append(path)
                return

            # Search children of current combination
            letters = digits_to_letters[digits[index]]
            for letter in letters:
                dfs(index + 1, path + letter)
            
        # Handle exception : No digit
        if len(digits) == 0:
            return []

        digits_to_letters = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        combinations = []

        # Call dfs from root node("")
        dfs(0, "")

        return combinations




        