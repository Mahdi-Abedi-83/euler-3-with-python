def aval(n):
    for i in range(2, int(n*0.5)+1):
        if n % i == 0:
            return False
    else:
            return True


def tagh(x):
    if me % x == 0:
        print(x)

me = 600851475143
for i in range(2, me+1):
    if aval (i):
        tagh(i) 
