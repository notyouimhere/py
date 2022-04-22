n1 = int(input("Enter number of student"))
i = []
n = []
student = {}
for j in range(0,n1):
    temp = input("Enter id for the student : ")
    temp = int(temp)
    i.append(temp)
    temp1 = input("Enter name for the student : ")
    n.append(temp1)


print(i)
print(n)

r = 0
l = len(i)
while (r < l):
    student[i[r]] = n[r]
    r = r + 1
print(student)
