from collections import deque

# Page Table Entry for Inverted Page Table


class PTE:
    def __init__(self, vpn: int, ref_time: int):
        self.vpn = vpn
        self.ref_time = ref_time


def LRU(reference_str: str, n_frames: int) -> int:
    frames = [[0 for _ in range(len(reference_str) + 1)] for _ in range(n_frames + 1)]
    frames[0] = ['-'] + [c for c in reference_str]

    # make inverted page table
    page_table = [PTE(0, 0) for _ in range(n_frames + 1)]
    page_table[0] = PTE(-1, -1)

    count = 0  # global counter for reference time
    page_fault = 0

    for c in reference_str:
        count += 1

        # check if the page is in the frame
        found = False
        for i in range(1, n_frames + 1):
            if page_table[i].vpn == int(c):
                found = True
                page_table[i].ref_time = count
                break

        # if not found,
        if not found:
            # find the least recently used page
            lru = 1
            for i in range(2, n_frames + 1):
                if page_table[i].ref_time < page_table[lru].ref_time:
                    lru = i

            # replace the page
            page_table[lru].vpn = int(c)
            page_table[lru].ref_time = count
            page_fault += 1

        # update frames
        for i in range(1, n_frames + 1):
            frames[i][count] = page_table[i].vpn

    print_frames(frames)
    return page_fault


def FIFO(reference_str: str, n_frames: int) -> int:
    frames = [[0 for _ in range(len(reference_str) + 1)] for _ in range(n_frames + 1)]
    frames[0] = ['-'] + [c for c in reference_str]

    # make inverted page table (FIFO Queue with size n_frames)
    page_queue = deque(maxlen=n_frames)

    page_fault = 0

    for i, c in enumerate(reference_str):
        # check if the page is in the frame
        found = False
        if c in page_queue:
            found = True

        # if not found,
        if not found:
            # if the page queue is full, pop automatically
            # append the page
            page_queue.append(c)
            page_fault += 1

        # update frames
        for f in range(1, n_frames + 1):
            if f <= len(page_queue):
                frames[f][i + 1] = page_queue[f - 1]

    print_frames(frames)
    return page_fault


def OPT(reference_str: str, n_frames: int) -> int:
    frames = [[0 for _ in range(len(reference_str) + 1)] for _ in range(n_frames + 1)]
    frames[0] = ['-'] + [c for c in reference_str]

    # make inverted page table
    page_table = [0 for _ in range(n_frames + 1)]
    n_pte = 0

    # make a dictionary for the next reference of each page
    next_ref = {}
    for i, c in enumerate(reference_str):
        if c not in next_ref:
            next_ref[c] = i

    page_fault = 0

    for i, c in enumerate(reference_str):
        # update the next reference of the page
        next_ref[c] = reference_str.find(c, i + 1)
        if next_ref[c] == -1:
            next_ref[c] = len(reference_str) + 1

        # check if the page is in the frame
        found = False
        for j in range(1, n_frames + 1):
            if page_table[j] == c:
                found = True
                break

        # if not found,
        if not found:
            page_fault += 1

            # if the page table is not full, append the page
            if n_pte < n_frames:
                n_pte += 1
                page_table[n_pte] = c
            # if the page table is full,
            else:
                # find the page that will not be used for the longest time
                longest = 1
                for j in range(2, n_frames + 1):
                    if next_ref[page_table[j]] > next_ref[page_table[longest]]:
                        longest = j

                # replace the page
                page_table[longest] = c

        # update frames
        for f in range(1, n_frames + 1):
            frames[f][i + 1] = page_table[f]

    print_frames(frames)
    return page_fault


def print_frames(frames: list) -> None:
    for i in range(len(frames)):
        for j in range(len(frames[i])):
            print(frames[i][j], end=' ')
        print()


if __name__ == '__main__':
    reference_str = '12342156212376321236'
    n_frames = [1, 2, 3, 4, 5, 6, 7]

    print("LRU")
    for n in n_frames:
        print("-" * 20)
        print(f'Number of frames: {n}')
        print(f'Number of page faults: {LRU(reference_str, n)}')

    print("FIFO")
    for n in n_frames:
        print("-" * 20)
        print(f'Number of frames: {n}')
        print(f'Number of page faults: {FIFO(reference_str, n)}')

    print("OPT")
    for n in n_frames:
        print("-" * 20)
        print(f'Number of frames: {n}')
        print(f'Number of page faults: {OPT(reference_str, n)}')
