def generate_sequences(K, N):
    # Helper function to generate sequences using recursion
    def backtrack(current_sequence):
        # If the sequence is of length N, add it to results
        if len(current_sequence) == N:
            results.append(current_sequence.copy())
            return
        # Try all possible numbers from 1 to K
        for i in range(1, K + 1):
            current_sequence.append(i)
            backtrack(current_sequence)
            current_sequence.pop()

    results = []
    backtrack([])
    return results


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    K = int(data[0])
    N = int(data[1])

    sequences = generate_sequences(K, N)

    for seq in sequences:
        print(' '.join(map(str, seq)))
