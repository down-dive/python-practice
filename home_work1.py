a = [i for i in range(1,20)]       #list comprehention...
print(a)                           #...for loop for working with iterables, datastructure

b = a[::-1]                        #reverce
print(b)

c = a[4:19:3]                      #start:end:step
print(c)

d = tuple(a)                       #tuple
print(d)

e = str(a)                         #string
print(type(e))



store = {                                            #dictionary
    "fruits":{"apples":10, "bananas":20, "oranges":30},
    "vegetables":{"potatoes":40, "carrots":50, "onions":60},
    "flour":{"bread":70, "bun":80, "pasta":90},
    }

for g in store.keys():                             #keys
    print(g)

for h in store.values():                           #values
    print(h)

for i in store.values():                          #values in keys
    for g in i.keys():
        print(g)

for k in store.values():                          #values in values
    for l in k.values():
        print(l)
        
m = list(store.keys())                            #list of keys
print(m)

n = list(store.values())                         #list of values
print(n)
    
for o in store.values():                         #list of keys in values
    print(list(o))


a = 20       
b = 30
c = 40

if a > b or c > b and b == c:   #if loop, when there is one...
    print("UaU")                #...or more conditions that should be met

elif a != b and a <= c:
    print("Ops")
    
else:
    print("Thats right")



while c != 50:                #while loop, while the condition is True it works
    print(c)
    break



def allnumbers(a,b,c):        #function
    return a + b + c
sum_numbers = allnumbers(12,34,56)

print(sum_numbers)




    






        








