#Evan Reynolds
#CSCI 101-B
#Create Project



#libraries needed
import math
import string
import time


#functions
def stringnum(strin):    #converts string to numbers
    sub=[]
    for i in range(0,len(strin)):
        j=str(strin[i])
        big=string.printable
        k=big.find(j)
        sub.append(k)
    return sub

def recode(code):        #turn code into list
    fix=[]
    for num in str(code):
        fix.append(int(num))
    return fix

def cycle(c):           #cycle n from (0,7)
    n=c
    if n==7:
        n=0
    elif n!=7:
        n+=1
    return n

def encode(listin,code):  #shifts numbers using code
    n=0
    fix=[]
    top=len(string.printable)
    num=recode(code)
    for ele in listin:
        if num[n]+ele>top:
            fix.append(ele-top+num[n])
        else:
            fix.append(ele+num[n])
        n=cycle(n)
    return fix

def numstring(numlist):    #converts list of numbers to string
    final=''
    for ele in numlist:
        final+=str(string.printable[int(ele)])
    return final

def decode(listin,code):   #shifts numbers back using code
    n=0
    fix=[]
    top=len(string.printable)
    num=recode(code)
    for ele in listin:
        if ele-num[n]<0:
            fix.append(ele+top-num[n])
        else:
            fix.append(ele-num[n])
        n=cycle(n)
    return fix

def writetxt(name,contents):#write text file
    new=open("name",'w+')
    new.write(contents)
    new.close()

def listrank(diction,check):#check the validity of a trial, diction is dictionary, check is object being checked
    rank=0
    for word in check:
        for item in diction:
            if item==word:
                rank+=1
                break
    return rank

def valcode(check):
    if len(str(check)) !=8:
        print("Error: more than 8 digits")
    if check<0:
        print("Error: negative encryption code")

def readfile(name):
    read=open(name,'r')
    ready=read.read()
    read.close()
    return ready



#find operation
print("This program only encrypts using a 8-digit encryption code")
opcode=int(input("Enter 1 if encrypting, 2 if decrypting, or 3 if breaking: "))



#create library of letters
chars=string.printable
length=len(chars)



#encrypting
if opcode==1:
    file=input("Enter file name here: ")
    code=int(input("Enter 8 digit encryption code here: "))
    valcode(code)
    ready=readfile(file)
    out=input("Give a name for decrypted file: ")
    writetxt(out,numstring(encode(stringnum(ready),code)))



#decrypting
if opcode==2:
    file=input("Enter file name here: ")
    code=int(input("Enter 8 digit decryption code here: "))
    valcode(code)
    ready=readfile(file)
    out=input("Give a name for encrypted file: ")
    writetxt(out,numstring(decode(stringnum(ready),code)))


#breaking
if opcode==3:
    file=input("Enter file name here: ")
    ready=readfile(file)
    poss=[]
    rank=[]
    for x in range(0,99999999):
        poss.append(numstring(decode(stringnum(ready),x)))
    for item in poss:
        rank.append(listrank(words,item))
    loc=rank.find(max(rank))
    print(poss[loc])
