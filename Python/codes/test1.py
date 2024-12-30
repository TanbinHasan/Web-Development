import sys

read = sys.stdin.readline
write = sys.stdout.write

for i in range(1, 11):
  write(f"{i}{' ' if i < 10 else ''}")