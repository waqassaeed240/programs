#Data types (Integers , float , complex number+j) // string list tuple // dictionary set
# mutable (List dictionery byte array)
# immutable (int float complex string tuple set)

a = 20
b = 2.2
c = 3+2j

print (a , (type(a)))
print (b , (type (b)))
print (c, (type(c)))

s = "h@3wnd"
print (s , type(s))

d = '''
my namee
        is waqas 
                saeed
'''
print (d , type(d))

# List (Mutable)
l = [10 , 'ws' , 2.3]
l[2]=3.3
print(l, type(l))

# tuple (immutale)

t =(10,2.2,'waqas')
print(t , (type(t)))

# Dictionary mutable
d = {
    'name' :        "Waqas saeed" ,
    'class' :       'MCS IT' ,
    'Roll Number' : '0081'
}
print(d['name'], type(d))

# set immutable unique value

s = {10,20,30,30}
print(s, type(s))
