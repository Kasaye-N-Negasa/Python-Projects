x = 0
for y in range(3):​
    x = x + 2​
    print("\ny = ",y,"x = ",x)​
    if x == 8:​
        continue​
    print('this line will be skipped over if x=8')​
