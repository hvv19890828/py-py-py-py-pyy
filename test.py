#!/usr/bin/python3
import mysql.connector
import requests
import logging
import time
import os
import json
import sys
import time
import re
import random as rmdm
from math import cos as c
import modulek as mod



r = requests.get('http://graph.facebook.com/')
print("Returning a kind of token after a Facebook API call" +  r.json()['error']['fbtrace_id'])


'''
docker run --name mysql-hvv --restart always --network host  -v ~/datadir:/var/lib/mysql  -v ~/datadir:/etc/mysql/conf.d  -e MYSQL_DATABASE=hvv  -e MYSQL_ROOT_PASSWORD=user1! -d mysql
'''
db = mysql.connector.connect(
     host="localhost",
     user="root",
     passwd="user1!",
     database="hvv",
     auth_plugin="mysql_native_password"
     )

mycursor = db.cursor()
#mycursor.execute("create table xerson (name varchar(50), age int, id int primary key auto_increment)")
#db.commit()
mycursor.execute("describe person")
for i in mycursor:
   print(i)
db.close()

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
#    pass

par_obj = mod.parent("par_obj mod.parent initiation with arg")
par_obj.func1(333333333333333)

child_obj = child("877","child_obj child initiation with second arg")
child_obj.child_func1("arg1 of child_obj.func1")



#-------------------------------------




with open("inptFl.json", mode='r+', encoding='utf_8') as jsonInptFl:
 jsonBffr = json.load(jsonInptFl, strict=False)

jsonOtptFl = open("otptFl.json", mode='r+', encoding='utf_8')

textets = jsonOtptFl.read()
rEx = re.findall(r"ip",textets)
print("print(x,rEx): ",rEx)
#json.dump(jsonBffr, jsonOtptFl)

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
dict = ({"dict1": "dict value"})
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
 print("finaly")
