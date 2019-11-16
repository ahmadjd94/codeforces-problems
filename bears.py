inpu  = input().split(" ")

limak = int(inpu[0])
bob = int(inpu[1])

i = 0

if limak <= bob:
    while True :
        limak = limak * 3
        bob = bob * 2
        i += 1

        if (limak > bob):
            break
print(i)