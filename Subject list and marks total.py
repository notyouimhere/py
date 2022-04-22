d1 = {}
d2 = {}
nm = []
m = []
roll = []
total = []
n1 = int(input(" Enter Number of students : " ))
for i in range(0,n1):
    n = input("Enter name of the student : " )
    r = int(input("Enter roll number of the student : "))
    nm.append(n)
    roll.append(r)
    j = 0
    if(j < 3):
        m1 = int(input("Enter marks of subject 1 : "))
        m2 = int(input("Enter marks of subject 2 : "))
        m3 = int(input("Enter marks of subject 3 : "))
        m.append(m1)
        m.append(m2)
        m.append(m3)
        t = m1 + m2 + m3
        total.append(t)
    j = j + 1
k = 0
for t in roll:
    d1[t] = nm[k]
    d2[t] = total[k]
    k = k + 1
print(roll)
print(nm)
print(m)
print(d1)
print(d2)

    
