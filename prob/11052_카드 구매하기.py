n = int(input())
p = [0] + list(map(int, input().split()))

# 4���� ���
# p1 + d[3], p2 + d[2], p3 + d[1], p4 + d[0]
# d[4] = ���� �ִ밪
d = [0] * (n+1)
for i in range(1, n+1):
    arr = []
    for j in range(1, i+1):
        arr.append(p[j] + d[i-j])
    d[i] = max(arr)

print(d[n])