class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(size):
            for i in range(start+1, start+size+1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True

        start = 0
        byte1 = 0b0
        byte2 = 0b110
        byte3 = 0b1110
        byte4 = 0b11110
        while start < len(data):
            first = data[start]
            if(first >> 3) == byte4 and check(3):
                start += 4
            elif(first >> 4) == byte3 and check(2):
                start += 3
            elif(first >> 5) == byte2 and check(1):
                start += 2
            elif(first >> 7) == byte1:
                start += 1
            else:
                return False
        return True
