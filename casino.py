def solution(n, k):
    # write your code in Python 3.6

    solutions_matrix = []
    for i in range(n+1):
        solutions_matrix.append([])
        for r in range(n+1):
            solutions_matrix[i].append({"v":1,"all":False} if i==0 and r ==0 else {})

    for i in range(n+1):
        for r in range(n+1):
            try:
                if not any(solutions_matrix[i][r+1]):
                    solutions_matrix[i][r + 1] = {"all": False}

                if not any(solutions_matrix[i][r * 2]):
                    solutions_matrix[i][r * 2] = {"all": True}
                # solutions_matrix[i][solutions_matrix[i][r]["v"]*2] = {"v": solutions_matrix[i][r]["v"], "all": True}
            except:
                pass

    col = 0
    row = 0


    for r in solutions_matrix:
        col = 0
        for c in r:

            print(col+1, row+1, solutions_matrix[col][row])
            col+=1
        row+=1




if __name__ == '__main__':
    solution(4,3)