class Solution(object):
    def characterReplacement(self, s, k):
        # sliding window question!
        # we have a left and a right 
        # our condition is that k is not exceeded 
        L = 0
        R = 0
        maxLength = 0
        currentLength = 0
        hashmap = {}

        while R < len(s):
            if s[R] in hashmap:
                hashmap[s[R]] += 1
            else:
                hashmap[s[R]] = 1

            # get the max value
            currentLength = R - L + 1
            g = max(hashmap.values())
            
            while (currentLength - g) > k:
                #shift down the L
                hashmap[s[L]] -= 1
                L += 1
                g = max(hashmap.values())
                currentLength = R - L + 1   

            currentLength = R - L + 1
            maxLength = max(maxLength, currentLength)
            R += 1
        return maxLength