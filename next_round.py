nums = input().split(" ")

contestants = input().split(" ")

target = int(contestants[int(nums[1]) -1 ])

passed = 0

for i in contestants:
    if int(i) >= target and int(i) > 0:
        passed += 1

print(passed)
