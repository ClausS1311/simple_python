def functie(num1, num2):
    return (num1+num2)/2


nr1 = int(input("nr este "))
nr2 = int(input("nr este "))
print(functie(nr1, nr2))

#apelare functie prin argument
# print(functie(5, 10))

def functie2(n1,n2):

    def func3(a1,a2):
        return (a1+a2)*(a1*a2)
    return func3(n1,n2)
print(functie2(nr1,nr2))

