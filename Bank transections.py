bank = {1:["charli" , 25000], 2 : ["Angel",5000], 3: ["Jolly", 2000]}
#print(bank)

tran = []
for ac in bank:
    ac = int(input("Enter account number : "))
    tran.append(ac)
    if(ac not in bank):
        print("Enter valid account number : " )
    else:
        t= input("Enter D for Deposite and W for withdraw : " )
        tran.append(t)
        if(t == 'W' or t == 'w'):
            amount = int(input("Enter the amount for withdraw : "))
            total = bank[ac][1] - amount
            tran.append("Amount = "+ str(amount))
            tran.append("Total = " + str(total))

            n=input("You want to transact more? Y/N : ")
            if(n == 'N' or n == 'n'):
                break
            elif(n == 'Y' or n == 'y'):
                continue
                
        elif(t == 'D' or t=='d'):
            amount = int(input("Enter the amount for deposite : "))
            depo = bank[ac][1] * 50 / 100
            
            if(amount < depo):
                total = bank[ac][1] + amount
                tran.append("Amount = "+ str(amount))
                tran.append("Total = " + str(total))
                n=input("You want to transact more? Y/N : ")
                if(n == 'N' or n == 'n'):
                    break
                elif(n == 'Y' or n == 'y'):
                    continue   
            else:
                message = "You can not enter more then " + str(depo)
                print(message)
                print(" Try Again ")
                
                n=input("You want to transacct more? Y/N : ")
                if(n == 'N' or n == 'n'):
                    break 
                elif(n == 'Y' or n == 'y'):
                    continue
            

print("****************************Transection Report************************")
#print(bank[ac])
print(str(tran) + "\n")
            
            
        
        
    

