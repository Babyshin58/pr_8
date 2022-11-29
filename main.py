import random

def password():
    s1 = ['a','b','c','d','e','g','h','f','z','x','c','v','p','n','m','o','k','r','q','w','r']
    s2 = ['A','B','C','D','E','G','H','F','Z','X','C','V','P','N','M','O','K','R','Q','W','R']
    s3 = ['1','2','3','4','5','6','7','8','9']
    result = ''
    for i in range(11):
        result += random.choice(s1+s2+s3)
    return result

p = password()
print(p)

