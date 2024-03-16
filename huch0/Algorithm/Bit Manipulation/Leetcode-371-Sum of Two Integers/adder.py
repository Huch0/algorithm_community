class Solution:
    def getSum(self, a: int, b: int) -> int:
        def half_adder(a, b):
            return (a ^ b, a & b)

        def full_adder(a, b, cin):
            s1, c1 = half_adder(a, b)
            s2, c2 = half_adder(cin, s1)
            cout = c1 | c2
            return (s2, cout)

        def ripple_carry_adder_12(a, b):
            MASK = 0xFFF  # The range of a and b is [-1000, 1000]
            MAX_INT = 0x7FF  # For handle negative numbers

            a_12 = a & MASK
            b_12 = b & MASK

            c = 0  # carry of each bit
            s = 0  # sum of a and b
            i = 0  # index
            while i < 12:
                # Calculate the sum and carry of each bit
                s_i, c = full_adder(a_12 & 1, b_12 & 1, c)
                s |= s_i << i  # Add s_i to s at the i-th bit

                a_12 >>= 1
                b_12 >>= 1
                i += 1

            # Confine the s to 12 bits
            s = s & MASK

            # Handle negative numbers (Fill the 1s to the left of the 12th bit)
            if s > MAX_INT:
                s = ~(s ^ MASK)

            return s

        return ripple_carry_adder_12(a, b)
