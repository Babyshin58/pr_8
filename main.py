import random

def password():
    s1 = ['a','b','c','d','e','g','h','f','z','x','c','v','p','n','m','o','k','r','q','w','r',]
    result = ''
    for i in range(11):
        result += random.choice(s1)
    return result

p = password()
print(p)
