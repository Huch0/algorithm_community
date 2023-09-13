class Solution:
    def isValid(self, s: str) -> bool:
        # hash map for pairing brackets
        bracket_pair_map = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        # stack for opening brackets
        open_brackets = []

        for c in s:
            if c in bracket_pair_map.values():
                open_brackets.append(c)
            else:
                if len(open_brackets) == 0:
                    return False
                if open_brackets.pop() != bracket_pair_map[c]:
                    return False
                    
        if len(open_brackets) > 0:
            return False

        return True
                