import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
trees = list(map(int, sys.stdin.readline().rstrip().split()))

left, right, height= 0, max(trees), 0
while left <= right:
    mid = (left + right)//2
    
    logs = 0 # �ڸ� ���� ��
    for tree in trees:
        if tree > mid:
            logs += tree - mid
    
    if logs >= m: # �ڸ� ���� ���� ������ �� ���� ����   
        height = mid
        left = mid + 1
    else:
        right = mid -1

print(height)     