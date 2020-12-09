#!/usr/bin/python3

#in case if facing issues with pip: curl https://bootstrap.pypa.io/get-pip.py | python3
import mysql.connector #pip3 install mysql-connector-python
import requests #pip3 install requests may be required
import logging
import time
import os
import json
import sys
import re
import random as rmdm
from math import cos as c
import modulek as mod
import argparse
import zipfile
from pathlib import Path
import threading


def generator():
    for i in range(6):
        yield i*i
g = generator()
for i in g:
    print(i)
print(str(g))



def outer_function():
    a = 5
    def inner_function():
        nonlocal a
        a = 10
        print("Inner fun: ",a)
    inner_function()
    print("Outer fun: ",a)

outer_function()

aglo = 13.3
bglo = 11
def improper_return_function():
    global bglo
    print("print bglo " + str(bglo))
    bglo = 13
    print("print bglo " + str(bglo))
    if (aglo % 2) == 0:
        return True
    else:
        return aglo % 2
x = improper_return_function()
print(x)
print("print bglo " + str(bglo))

b = 1
a = [ b , 2 , 3 ]
del b
print(str(tuple(a)))


def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'*'*(2*x+1))    
pyfunc(9)


try:
 r = requests.post('http://graph.facebook.com/')
 print("Returning a kind of token as a result of a Facebook API test call " +  r.json()['error']['fbtrace_id'])
except:
 print("well ... it seems that there is no network connection ... not a really big deal .. but you know me .. I'm already pissed off ")
 

'''

docker run --name mysql-hvv --restart always --network host  -v ~/datadir:/var/lib/mysql  -v ~/datadir:/etc/mysql/conf.d  -e MYSQL_DATABASE=hvv  -e MYSQL_ROOT_PASSWORD=user1! -d mysql

'''

try:
 db = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="user1!",
     database="hvv",
     auth_plugin="mysql_native_password"
     )

 mycursor = db.cursor()
 try:
  mycursor.execute("create table xerson (name varchar(50), age int, id int primary key auto_increment)")
 except:
  print("now .. I'm almost sure that such table name is already occupied in this db .. so consider choosing another one ... but fck man why shold I monitor this shit? start being more attentive ...")
#db.commit()
 mycursor.execute("describe xerson")
 for i in mycursor:
   print(i)
 db.close()
except:
 print("ok ... looks like there is no db connected ... but anyway fuck that and go on ...")

"""

\d = any digit
\D = any non digit
\w = any alphabet symb
\W = any non alphabet symb
\s = any space
\S = any non space

"""

testText = "tvm1wewxcewew" \
            "fdfdfd342343243fdfdf" \
            "sfdfsfsfsfsfsf"
textSchema = r"342343243"
rEx = re.findall(textSchema,testText)
print("print(x,rEx): ",rEx)




print("printed cos from 7 as 'c'",c(7))

class child(mod.parent):
  def __init__(self, arg1, arg2):
    super().__init__(arg2) 
    print("printed arg1 from child init ",arg1)
  def child_func1(self, arg1):
     print("printed arg1 from child child_func1", arg1)
     self.func1(434)
  forFun = "to be returned from fun"
  def fun(self): 
    return self

#    pass

par_obj = mod.parent("par_obj mod.parent initiation with arg")
par_obj.func1(333333333333333)

child_obj = child("877","child_obj child initiation with second arg")
print(child_obj.child_func1("arg1 of child_obj.func1"))
print(child_obj.fun().forFun)
print(mod.parent("independent parent").func1(67676))
#-------------------------------------




with open("inptFl.json", mode='r+', encoding='utf_8') as jsonInptFl:
 jsonBffr = json.load(jsonInptFl, strict=False)

jsonOtptFl = open("otptFl.json", mode='r+', encoding='utf_8')

textets = jsonOtptFl.read()
rEx = re.findall(r"ip",textets)
print("print(x,rEx): ",rEx)
#json.dump(jsonBffr, jsonOtptFl)

jsonInptFl.close()
jsonOtptFl.close()




#------------------------------------

print("just a print")
print("3-9: ",3-9)
print((" 9 // 3: ", 9 // 3))
print("remainder 9 % 4: ",9 % 4)
print("rise 9 to the 6 power: ",9 ** 6)


just_an_str = "just_an_str"
just_an_int = 23
print("print str (float(js)),just_an_str): ",str (float(just_an_int)),just_an_str)

inpt = str(500) # input("enter firstjhh:")

print("print inpt + just_an_str: ",inpt + just_an_str)


if inpt == str(0):
   print("if inpt == str(0):")
elif inpt != str(1):
  print("elif inpt != str(1):")
else:
 print("else:")

for i in inpt:
   print("Print from for loop: ",i, "\n")

j=0
while j < 10:
   print("Print from while loop: ",j)
#   j-=1
   j+=1


arry = [32323,545445,232535,["no,d",3,3434.4344,[{"wew": "uyuyuuyu"}]]]
cort = ("dasdsd",'sdsds',2323)
dict = {"dict1": "dict value"}
print("print("", dict['dict1'])" + dict['dict1'])
plur = {"434","erer"}


def xoxo(stri):
  return stri
xoxo(inpt)

try:
 lya =  lambda x, y: print(x - y)
 lya(int(inpt), float(inpt))
except:
 print("except: r u fcking out of your fcking mind, and don't you see it acceps integer value only!!!?")
else:
 print("else")
finally:
 print("finaly crcleci")
