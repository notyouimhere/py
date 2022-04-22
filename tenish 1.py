p1=input("name of player1:")
p2=input("name of player2:")
st=int(input("best of 3 or best of 5 : "))
ch ='y'
res=[]
while(ch == 'y'):
    t1=int(input("enter game won by player 1 : "))
    t2=int(input("enter game won by player 2 : "))
    res.append(t1)
    res.append(t2)
    ch=input("do you want to continue?(y or n): ")
print(res)
ps1=0
ps2=0
for i in range(0,len(res),2):
    if(res[i] > res[i+1]):
        ps1 = ps1 + 1
        
    else:
        ps2 = ps2 + 1
    
print("Total set won by player 1 : "+str(ps1))
print("Total set won by player 2 : "+str(ps2))
if(ps1 > ps2):
    print(p1+ " ---player 1 won---")
else:
    print(p2+ " ---player 2 won---")
pg1=0
tot = sum(res)
print("Total game played by both player : "+str(tot))
for i in range(0,len(res),2):
    pg1 = pg1 + res[i]
print("Total games played by player 1 : "+str(pg1))
print("Total games played by player 2 : "+str(tot-pg1))





