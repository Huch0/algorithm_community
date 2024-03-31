class Solution:
    def validUtf8(self, data: list[int]) -> bool:
        def check(bytes):
            for i in range(bytes):
                if start + 1 + i >= len(data):
                    return False
                if data[start + 1 + i] & 0xC0 != 0x80:
                    return False
            return True
        
        start = 0
        while start < len(data):
            if data[start] & 0x80 == 0:
                start += 1
            elif data[start] & 0xE0 == 0xC0 and check(1):
                start += 2
            elif data[start] & 0xF0 == 0xE0 and check(2):
                start += 3
            elif data[start] & 0xF8 == 0xF0 and check(3):
                start += 4
            else:
                return False
        if start != len(data):
            return False
        return True