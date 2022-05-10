str1 = input()
str2 = str1 [2:]
l = len(str2)
'''
dic = {'A':10, 'B':11,'C':12,'D':13,'E':14,'F':15}
x1 = 0
n1 = l - 1
for word in str2:
    if word in dic:
        x1 = x1 + int(dic[word])*16**n1
    else:
        x1 = x1 + int(word)*16**n1
    n1 = n1 - 1
print(x1)
'''
print('str2: ',l)