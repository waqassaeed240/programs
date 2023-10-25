# Itrate over 2 plus lists at the same the 
l = [10,20,30,40,50]
l1 = [12,42,45,32]

for a,b in zip(l,l1):
    print(a,b)

# String convert into list
a = input("Enter the value:- ")

l=a.split()
print(l)