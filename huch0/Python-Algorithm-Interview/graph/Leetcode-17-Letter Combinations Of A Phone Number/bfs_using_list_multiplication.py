class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        if len(digits) == 0:
            return []

        combinations = [""]

        for digit in digits:
            new_letters = digits_to_letters[digit]
            # Store previous length of combinations 
            prev_len = len(combinations) 
            # Duplicate current combinations 
            combinations *= len(new_letters)

            for i in range(len(new_letters)):
                for j in range(len(combinations)):
                    # Regard each part of duplicated combinations seperately 
                    if j // prev_len == i:
                        # Add new letter in the end of the combination string
                        combinations[j] += new_letters[i]



        return combinations




