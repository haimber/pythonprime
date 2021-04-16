prime_lst = [2]
x = 2
while True:
    x = x + 1
    for i in prime_lst:
        if (x % i) == 0:
            break
        if i == prime_lst[-1]:
            prime_lst.append(x)
            print(x)



