length = int(input())

problems = []
for i in range(length):
    problems.append(input().split(" "))

solvable = 0

for arr in problems:
    if (arr[1] == "1" and arr[0] == "1") or (arr[1] == "1" and arr[2] == "1") or (arr[0] == "1" and arr[2] == "1"):
        solvable += 1

print(solvable)
