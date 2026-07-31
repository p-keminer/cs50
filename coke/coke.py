sum = 0
allowed = [1,2,5,10,20,50]
while True:
    if sum >= 50:
        print("Change Owed: " + str(sum-50) )
        break
    print("Amount Due: " + str(50-sum))
    cash = int(input("Insert Coin: "))
    if cash != allowed:
        print("Amount Due: " + str(50-sum) )
    sum = sum + cash
