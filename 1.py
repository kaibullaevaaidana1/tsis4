s1 = input()
s2 = input()
p = input()
n = len(s1)
m = len(p)

mod = 10**9 + 7
base = 31

power = [1] * (m + 1)

for i in range(1, m + 1):
    power[i] = (power[i - 1] * base) % mod

def make_hash(s):
    h = [0] * (len(s) + 1)

    for i in range(len(s)):
        h[i + 1] = (h[i] * base + ord(s[i])) % mod

    return h

def get_hash(h, left, right):
    return (h[right] - h[left] * power[right - left]) % mod

h1 = make_hash(s1)
h2 = make_hash(s2)
hp = make_hash(p)

target = get_hash(hp, 0, m)

answer = 0

for i in range(n - m + 1):
    if i + m > len(s2):
        break

    hash1 = get_hash(h1, i, i + m)
    hash2 = get_hash(h2, i, i + m)

    if hash1 == target and hash2 == target:
        answer += 1
print(answer)
