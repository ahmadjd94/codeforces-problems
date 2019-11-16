summands = [int(i) for i in input().split("+")]
summands.sort()

print("+".join([str(i) for i in summands]))
