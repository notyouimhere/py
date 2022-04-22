cd = {1:234,2:350,3:123,4:560}
n = ["madhav","jolly","molly","polly"]
cust_type = ["c","d","d","c"]
j = 0
for i in cd.keys():
    temp = cd[i]
    if(temp > 501):
        r = 7.5
        t = 18
    elif((temp >=301) and (temp < 500)):
        r = 5.5
        t = 15
    else:
        r = 3.5
        t = 12
    amt = temp * r
    amt = amt + ((amt * t)/100)
    k = cust_type[j]
    if(k == "c"):
        amt = amt + ((amt * 10)/100)
    else:
        amt = amt - ((amt * 5)/100)
    print(n[j] + "  " + k + "  "  + str(amt))
    j = j + 1



