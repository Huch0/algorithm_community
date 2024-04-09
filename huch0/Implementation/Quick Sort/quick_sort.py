def quick_sort(seq: list, start: int, end: int) -> None:
    """
    in-place quick sort
    :param seq: A sequence of elements
    :param start: The index of the first element in the sequence
    :param end: The index of the last element in the sequence
    :return: None
    """
    if start >= end:  # No need to sort further
        return
    # Find the partition index
    pi = partition(seq, start, end)
    # Recursively sort the left and right sub-sequences
    quick_sort(seq, start, pi - 1)
    quick_sort(seq, pi + 1, end)


def partition(seq: list, start: int, end: int) -> int:
    """
    partition the sequence into two parts
    :param seq: A sequence of elements
    :param start: The index of the first element in the sequence
    :param end: The index of the last element in the sequence
    :return: The index of the pivot
    """
    pivot = seq[end]  # Pick the last element as the pivot
    left = start
    right = end - 1
    while left <= right:
        while left <= right and seq[left] <= pivot:
            left += 1  # Treat the element as LESS than the pivot
        while left <= right and seq[right] >= pivot:
            right -= 1  # Treat the element as GREATER than the pivot
        # Put the elements in the correct partition
        if left < right:
            seq[left], seq[right] = seq[right], seq[left]

    # Put the pivot in the middle of the two partitions
    seq[left], seq[end] = seq[end], seq[left]

    return left


if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))

    if len(seq) != n:
        raise ValueError("The number of elements is not equal to n")

    quick_sort(seq, 0, n - 1)

    print(" ".join(map(str, seq)))
