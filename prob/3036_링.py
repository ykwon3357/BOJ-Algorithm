def gcd(a, b): # ��Ŭ���� ȣ����
    if b == 0:
        return a
    return gcd(b, a%b)

n = int(input())
ring = list(map(int, input().split()))
for i in range(1, len(ring)):
    gcdring = gcd(ring[0], ring[i])
    print('{}/{}'.format(ring[0]//gcdring, ring[i]//gcdring))