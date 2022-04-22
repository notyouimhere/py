name = []
final = []
value = []
main = []
n = int(input("Enter number of students you want : "))
for i in range(n):
    n1 = input("Enter name of the student: ")
    name.append(n1)
    n2 = int(input("How many values : "))
    if(n2%3==0):
        for j in range(n2):
            v = int(input("Enter value : "))
            value.append(v)
        final.append(value)
        value = [] 
    else:
        print("For " + str(n1) + " The value must be in multiplication of 3")
        print("Please try again!!")
print(name)
print(final)
