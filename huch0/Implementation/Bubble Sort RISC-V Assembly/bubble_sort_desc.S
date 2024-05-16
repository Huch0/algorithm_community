.option norelax

.globl    array_size
.globl    array_start

.text
.globl _start

_start:
    la  a1, array_size
    lw  a1, 0(a1)
    la  a0, array_start

    bubble_sort:
        slli    t0, a1, 2       // t0 = 4 * n
        addi    t0, t0, -4      // t0 = 4 * (n - 1)
		add     t0, a0, t0      // last = &arr[n - 1]
    LOOP_I:
        add     t1, a0, x0      // cur = &arr[0]
        lw      t4, 0(t1)       // arr_j = arr[0]
    ZERO_SWAP:
        lw      t3, 4(t1)       // t3 = *(cur + 1)
        addi    t1, t1, 4       // cur++
        blt     t4, t3, SWAP  // if arr_j < *(cur + 1) goto SWAP
        add     t4, x0, t3      // arr_j = *(cur + 1)
        blt     t1, t0, ZERO_SWAP  // if cur < last, goto ZERO_SWAP
        beq     x0, x0, EXIT_I  // if no swap occured in inner loop, sort done
    LOOP_J:
        lw      t3, 4(t1)       // t3 = *(cur + 1)
        addi    t1, t1, 4       // cur++
        bge     t4, t3, NO_SWAP  // if arr_j >= *(cur + 1) goto NO_SWAP
    SWAP:
        sw      t4, 0(t1)       //  *(cur + 1) = arr_j
        sw      t3, -4(t1)       //  *cur = *(cur + 1)
        blt     t1, t0, LOOP_J  // if cur < last, goto LOOP_J
    NO_SWAP:
        add     t4, x0, t3      // arr_j = *(cur + 1)
        blt     t1, t0, LOOP_J  // if cur < last, goto LOOP_J
    EXIT_J:
        addi    t0, t0, -4      // last--
        bgt     t0, a0, LOOP_I  // if last > &arr[0], goto LOOP_I
    EXIT_I:


//Final infinite loop
end_loop:
	fence           // flush cache memory
	ebreak          // stop the simulator
	j end_loop


.data
// .align    2 // not supported by qtrvsim yet

array_size:
.word	30
array_start:
.word	93, 3, 98, 31, 44, 89, 6, 2, 95, 15, 18, 22, 58, 92, 27, 10, 40, 32, 9, 47, 81, 12, 7, 74, 79, 5, 43, 78, 13, 70

// Specify location to show in memory window
#pragma qtrvsim focus memory array_size
