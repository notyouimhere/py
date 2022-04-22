#max marks among number of student
sub = ("Maths","Science","English") #subjects are created 
n =int(input("enter number of students : ")) #asking user for number of user
roll = [] #created array to store the values of roll no
name = [] #created array to store the values of names
result = {}
for i in range(n): #for loop will run and take inputs of roll no, names and marks 
    r = input("enter roll number of the student : ")
    r = int(r)
    n1 = input("Enter name of the student : ")
    roll.append(r)
    name.append(n1)
    m1 = input("enter marks of maths : ")
    m1 = int(m1)
    m2 = input("enter marks of science : ")
    m2 = int(m2)
    m3 = input("enter marks of english : ")
    m3 = int(m3)
    temp = (m1,m2,m3) # marks are stored in temparary variable
    result[r] = temp
print(result)
mt = []
sc = []
eng = []
for j in result.keys():
    t = result[j]
    mt.append(t[0])
    sc.append(t[1])
    eng.append(t[2])
mh = max(mt)
sh = max(sc)
eh = max(eng)
for j in result.keys():
    t = result[j]
    if(t[0] == mh):
        print("Maths")
        print(mh)
        te = roll.index(j)
        print(name[te])
    if(t[1] == sh):
        print("Science")
        print(sh)
        te = roll.index(j)
        print(name[te])
    if(t[2] == eh):
        print("english")
        print(eh)
        te = roll.index(j)
        print(name[te])
