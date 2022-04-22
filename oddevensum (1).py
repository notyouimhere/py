j = []
ip = input("Enter how many values you want to enter in list: ")
ip = int(ip)
for i in range(ip):
    k = input("Enter values:- ")
    k = int(k)
    j.append(k)

sum_even =0
sum_odd = 0
i = 0 
while(i < len(j)):
    if(j[i] % 2 == 0):
        sum_even = sum_even + j[i]
    else:
        sum_odd = sum_odd + j[i]
    i = i + 1
    
print(j)
print("Sum of even numbers :- ",sum_even)
print("Sum of odd numbers :- ",sum_odd)  
