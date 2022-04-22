# search charechter from the list of name and count it

l = []
n = int(input("Enter number of names to be entered into the list"))
se = input("Enter search charechter you want ?")
i = 0
while i < n:
    temp = input("Enter names : ")
    #l.insert(i,temp)
    l.append(temp)
    i = i + 1

i = 0
ct = 0
for i in l:
    for j in  i:
        if j == se:
            ct = ct + 1
        print(i)
        print(ct)
        ct = 0
