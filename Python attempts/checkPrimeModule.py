def checkIfPrime (number) :
    for x in range (2, number) :
        if (number%x==0) :
            return False
        return True
answer = checkIfPrime(13)​
print (answer)
