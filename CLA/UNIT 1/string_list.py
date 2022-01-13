list=[]
for i in range(299):
    list.append(i+1)
print(list)  

def carre(a):
    return a**2    
# print first the length
print(len(list))
#squared values of the list
for i in list :
  print(carre(i))
#check if 57 is in the list
print(57 in list) 
