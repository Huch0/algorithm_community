# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# origin solution :
# https://leetcode.com/problems/path-sum-iii/solutions/141424/python-step-by-step-walk-through-easy-to-understand-two-solutions-comparison/?envType=study-plan-v2&envId=top-100-liked
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # define global result and path
        self.result = 0
        cache = {0: 1}

        # recursive to get result
        self.dfs(root, targetSum, 0, cache)

        return self.result

    def dfs(self, root, targetSum, currPathSum, cache):
        if root is None:
            return

        # print(cache)

        # currPathSum : Sum of node values from root to current node
        # Theorem
        # If within this path, there is a valid solution,
        # then there must be a oldPathSum such that currPathsum - oldPathsum = target

        # calculate currPathSum and required oldPathSum
        currPathSum += root.val
        oldPathSum = currPathSum - targetSum

        # update result and cache
        self.result += cache.get(oldPathSum, 0)  # add the number of paths that have oldPathSum
        cache[currPathSum] = cache.get(currPathSum, 0) + 1

        # dfs breakdown
        self.dfs(root.left, targetSum, currPathSum, cache)
        self.dfs(root.right, targetSum, currPathSum, cache)

        # when move to a different branch, the currPathSum is no longer available, hence remove one.
        cache[currPathSum] -= 1
