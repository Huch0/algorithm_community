class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        BYTE_MASK = 0xFF
        FOL_MASK = 0xC0  # Following bits mask

        count = 0  # count of following bytes
        for c in data:
            byte = c & BYTE_MASK

            if count > 0:  # Check if there are following bytes
                fol = byte & FOL_MASK
                if fol != 0x80:  # 0x10xxxxxx is expected
                    return False

                count -= 1  # Decrease count of following bytes
            else:
                isb = byte >> 7  # ith significant bit
                i = 0
                while isb != 0 and i < 5:
                    i += 1
                    isb = (byte >> (7 - i)) & 1

                if i == 1 or i == 5:
                    return False

                count = max(0, i - 1)

        # Check if there are remaining following bytes
        return count == 0
