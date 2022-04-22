store = []

st = int(input("Enter how many number you want to add : "))
if(st%2 ==0):
    for i in range(st):
        temp = int(input("Enter value : "))
        store.append(temp)
    print(store)
    ans = [] 
    for i in range(0,len(store),2):
        temp1 = [store[i],store[i+1]]
        temp2 = [store[i]+store[i+1]]
        ans.append(temp1)
        ans.append(temp2)
        temp1 = []
    print(ans)
else:
    print("Entered list must be Even in lenght")


   
    

