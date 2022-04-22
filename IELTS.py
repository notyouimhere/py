los = ("Speaking","Listening","writing","Reading")
c_no = []
name = []
module = []
overall = []
score = {}
n = int(input("Enter number of candidate = " ))

for i in range(n): 
    r = input("Enter Candidate number of the student : ")
    r = int(r)
    n1 = input("Enter name of the student : ")
    c_no.append(r)
    name.append(n1)
    s1 = input("enter score of Speaking : ")
    s1 = int(s1)
    s2 = input("enter score of Listening : ")
    s2 = int(s2)
    s3 = input("enter score of Writing : ")
    s3 = int(s3)
    s4 = input("enter score of Reading : ")
    s4 = int(s4)
    temp = (s1,s2,s3,s4)
    total = s1+s2+s3+s4
    ol = total / 4
    overall.append(ol)
    score[r] = temp
print(score)
print(c_no)
print(name)
print(overall)
S = []
L = []
W = []
R = []
for j in score.keys():
    t = score[j]
    S.append(t[0])
    L.append(t[1])
    W.append(t[2])
    R.append(t[3]) 
Sh = max(S)
Lh = max(L)
Wh = max(W)
Rh = max(R)
for j in score.keys():
    t = score[j]
    if(t[0] == Sh):
        print("Speaking")
        print(Sh)
        te = c_no.index(j)
        print(name[te])
    if(t[1] == Lh):
        print("Listening")
        print(Lh)
        te = c_no.index(j)
        print(name[te])
    if(t[2] == Wh):
        print("Writing")
        print(Wh)
        te = c_no.index(j)
        print(name[te])
    if(t[2] == Rh):
        print("Reading")
        print(Rh)
        te = c_no.index(j)
        print(name[te])
for k in score:
    if(k >= 6):
        print("Candidate is Qualified")
        print(k)
    elif(k < 6):
        print("Candidate is not Qualified")
        print(k)



        
    
