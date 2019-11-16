import random
d = input().split(" ")

width = int(d[0])
height = int(d[1])

matrix = []

for i in range(height):
    matrix.append([])

for row in matrix:
    for cell in range(width):
        row.append({"flag": False})


consumed_flags = set()

for i in range(height):
    for r in range(width):
        flag = random.randint(0, 2**32)

        if not matrix[i][r].get("flag"):
            matrix[i][r]["flag"] = flag

            try:
                if flag not in consumed_flags:
                    next_cell_in_row = r+1 < width
                    next_cell_in_col = i+1 < height

                    if next_cell_in_row and not matrix[i][r+1].get("flag", 0):
                        matrix[i][r + 1]["flag"] = flag
                        consumed_flags.add(flag)
                    elif next_cell_in_col and not matrix[i+1][r].get("flag", 0):
                        matrix[i+1][r]["flag"] = flag
                        consumed_flags.add(flag)
            except IndexError as exc:
                continue




print(len(consumed_flags))