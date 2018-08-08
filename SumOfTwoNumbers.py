"""
Hackerrank: read from STDIN

raw_input: read a line from STDIN and returns a string

number per line:
n = int(raw_input())

space-seperated numbers in line:
arr = map(int, raw_input().strip().split())

space-seperated str in line:
arr = map(str, raw_input().strip().split())

In Python3: Use input() instead of raw_input()

"""
t = int(raw_input())
for _ in range(t):
    a, b = map(int, raw_input().strip().split(' '))
    print a+b
