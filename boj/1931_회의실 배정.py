import sys

meetings = []

n = int(sys.stdin.readline().rstrip())
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    meetings.append((start, end))

# ȸ�� ���۽ð�, ����ð� ������ ���� ����
meetings.sort(key = lambda x : x[0])
meetings.sort(key = lambda x : x[1])

endTime, ans = 0, 0
for start, end in meetings:
    if endTime <= start: # ���۽ð��� ����ð� ���ĸ�
        endTime = end # ����ð� �ֽ�ȭ
        ans += 1 # ȸ�� �� ����

print(ans)
