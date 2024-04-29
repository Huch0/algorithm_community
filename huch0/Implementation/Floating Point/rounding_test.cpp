#include <iostream>
#include <bitset>

union FloatIntUnion
{
    float f;
    uint32_t i;
};

int main()
{
    FloatIntUnion a_bits;
    a_bits.i = 0b01000000100100000000000000000000;
    // 1.001 * 2^2 = 4.5
    // 0 | 1000 0001 | 0010 0000 0000 0000 0000 000
    float a = a_bits.f;
    std::cout << std::bitset<32>(a_bits.i) << std::endl;
    std::cout << a << std::endl;

    FloatIntUnion b_bits;
    b_bits.i = 0b01000000001000000000000000000011;
    // 1.010,0000,0000,0000,0000,0011 * 2^1 = 2.5
    // 0 | 1000 0000 | 0100 0000 0000 0000 0000 011
    // G : 1, R: 1, S: 0
    float b = b_bits.f;
    std::cout << std::bitset<32>(b_bits.i) << std::endl;
    std::cout << b << std::endl;

    FloatIntUnion b_1_bits;
    b_1_bits.i = 0b01000000001000000000000000000011;
    // 1.010,0000,0000,0000,0000,0011 * 2^1 = 2.5
    // 0 | 1000 0000 | 0100 0000 0000 0000 0000 001
    // G : 0, R: 1, S: 0
    float b_1 = b_1_bits.f;
    std::cout << std::bitset<32>(b_1_bits.i) << std::endl;
    std::cout << b_1 << std::endl;

    FloatIntUnion sum_bits;
    float sum = a + b;
    sum_bits.f = sum;
    std::cout << std::bitset<32>(sum_bits.i) << std::endl;
    std::cout << sum << std::endl;

    FloatIntUnion sum_1_bits;
    float sum_1 = a + b_1;
    sum_1_bits.f = sum_1;
    std::cout << std::bitset<32>(sum_1_bits.i) << std::endl;
    std::cout << sum_1 << std::endl;

    return 0;
}