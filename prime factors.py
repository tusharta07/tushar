def prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return 0
                break
        else:
            return 1

n=int(input("enter the number:"))

def primefac(a):

    for j in range(2,a-1):
        if prime(j)==1 and a%j==0:
            print (j)

prime_factors = [primefac(n)]
