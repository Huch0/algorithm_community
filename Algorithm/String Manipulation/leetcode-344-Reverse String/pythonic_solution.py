class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse() # or s[:] = s[::-1]
  """
  cuz of space complexity restriction, 
  It can't be solution >> s = s[::-1]
  (new object created and assigned)
  """
