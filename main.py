def Pr(num1:int,num2:int):
    '''
    find_prime that takes in 2 parameters and print the prime numbers between them
    '''
    for i in range(num1, num2+1):
        for j in range(2,i): 
            if (i%j) == 0:
             break
        else: 
            print(i)
Pr(10,70)
print(Pr.doc)