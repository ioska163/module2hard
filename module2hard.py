while True:
    n = []
    a = int(input('Введите число от 3 до 20:' ))
    if a > 2 and a < 21:
        for j in range(1, a):
            for k in range(1, a):
                if a % (j+k)==0 and j < k:
                    n.append(j)
                    n.append(k)
    print("result", n)



