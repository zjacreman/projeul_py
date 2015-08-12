# Project Euler problem 14
# Which starting number under one million produces the longest chain?

long_seq = 0
winner = 0

# Dynamic programming to the rescue!
MEMO = {1: 1, 2: 2}

def find_seq_len(num):
    n = num
    seq_len = 1
    while True:
        if n in MEMO:
            MEMO[num] = MEMO[n] + seq_len
            return MEMO[num]
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        seq_len += 1

for num in range(3, 1000000):
    seq_len = find_seq_len(num)
    if seq_len > long_seq:
        long_seq = seq_len
        winner = num

print(winner, long_seq)


