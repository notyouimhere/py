los = ("Chemistry","Biology","Maths","English")
n = input("Enter number of students to enter:")
n = int(n)
rl = [1,2,3]
nm= ["Colin","Rechard","mike"]
slist= {1:["Chemistry","Biology","Maths"],2:["Maths","English"],3:["Biology","English"]}
smark = {1:[70,80,80],2:[33,55],3:[60,70,90]}
#slist={}
#smark={}
#t1 = []
#t2 = []
for i in range(n):
    r = input("Enter Roll:")
    r = int (r)
    n1 = input("Enter name:")
    rl.append(r)
    nm.append(n1)
    print("Enter for Student:" + n1)
    k = input("Enter no of subjects:")
    k = int(k)
    #if 4 subject, 4 times name & mark of student
    for d in range(k):
        sn = input("Name of the subject:")
        sm = input("Marks of the subject:")
        sm = int(sm)
        t1.append(sn)
        t2.append(sm)
    slist[r] = t1
    smark[r] = t2
    t1 = []
    t2 = [] 
#print(slist)
#print(smark)
i = 0
t1 = []
t2 = []
k = 0
for i in rl:
    t1 = slist[i]
    t2 = smark[i]
    tot = sum(t2)
    h = rl.index(i)
    for j in los:
        if(j not in t1):
            k = los.index(j)
            t1.insert(k,"AB")
            t2.insert(k,"AB")
    print(nm[h]+" "+ str(t2) +" " +str(tot))
    

        

        

    
    
