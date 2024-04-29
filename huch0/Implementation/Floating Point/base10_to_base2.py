def base10_to_base2(x: float) -> str:
    base2_x = ""
    sign = ""

    # Handle negative numbers
    if x < 0:
        sign = "-"
        x = -x

    # Get the integer part
    i = int(x)
    while i > 0:
        base2_x = str(i % 2) + base2_x
        i //= 2

    if base2_x == "":
        base2_x = "0"
    base2_x += "."

    base2_x = sign + base2_x

    # Get the fractional part
    f = x - int(x)

    if f == 0:
        base2_x += "0"
        return base2_x

    while f > 0:
        f *= 2
        if f >= 1:
            base2_x += "1"
            f -= 1
        else:
            base2_x += "0"

    return base2_x


def base2_to_base10(x: str) -> float:
    sign = 1
    if x[0] == "-":
        sign = -1
        x = x[1:]

    x = x.split(".")
    int_part = x[0]
    frac_part = x[1]

    int_part = int(int_part, 2)
    frac_part = sum([int(frac_part[i]) * 2 ** -(i + 1)
                    for i in range(len(frac_part))])

    return sign * (int_part + frac_part)


def test_conversions(base10: float) -> None:

    base2 = base10_to_base2(base10)
    base2_10 = base2_to_base10(base2)
    print(base10, base2, base2_10)
    assert base10 == base2_10


if __name__ == "__main__":
    test_conversions(0.625)
    test_conversions(-10)
    test_conversions(0.4150390625)
    A = -8.0546875
    B = -0.179931640625
    test_conversions(A)
    test_conversions(B)
    test_conversions(A * B)
    test_conversions(65519)
    test_conversions(65504)

    print(base2_to_base10("1.011100110"))
