def create_string(value):
    s=""
    for i in range (6):
      s+=chr(value)
    return s
#main
for i in range(97,123):
    s=create_string(i)
    print(s)
    place=6
    while(place>0):
        place=place-1
        for j in range(97,123):
            lst=list(s)
            lst[place]=chr(j)
            print("".join(lst))
        


            
