def number_of_zeros_1(n):
    quantitly = 0
    while abs(n)>0:
        if quantitly >= 3:
            return True
        elif n % 10 == 0:
            quantitly+=1
        n=abs(n)//10
    return False

def number_of_zeros_2(n):
    quantitly = str(n).count("0")
    if quantitly >= 3:
        return True
    return False
