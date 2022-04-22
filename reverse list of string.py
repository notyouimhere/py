# reverse string in list
List = ["DEEP","SHETA","Bsc IT" ,"Student"]

print("Origenal list of strings are :" + str(List))

res = [i[::-1] for i in List]

print("Reverse list is :")
print(str(res))
