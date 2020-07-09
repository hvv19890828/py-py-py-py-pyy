import time
import os
import json
import sys
import time
import re
import random as rmdm
from math import cos as c
import modulek as md

print(c(7))

class srkf (md.Car):
  def __init__(self,w):
     print("initnax ",w)
  def blab(self, fjh):
     print(fjh)
     self.bla(434)
#    pass

rrrr = md.Car()
rrrr.bla(333333333333333)

rrr = srkf("877")
rrr.blab("4yty334")



#-------------------------------------




jsonInptFl = open("/root/inptFl.json", mode='r+', encoding='utf_8')


jsonBffr = json.load(jsonInptFl, strict=False)

jsonOtptFl = open("/root/OtptFl.json", mode='r+', encoding='utf_8')

json.dump(jsonBffr, jsonOtptFl)

jsonOtptFl.close()

jsonInptFl.close()




#------------------------------------

print("jdhejdhejhd")
print(3-9)
print((9 // 3))
print(9 % 4)
print(9 ** 6)


hg = " dsd"
js = 23
print("fdfjdjfhjd ",str (float(js)),hg)
nud = input("enter firstjhh:")
print(nud + hg)


if nud == str(0):
   print("DADADA")
elif nud != str(1):
  print("pasiryodke")
else:
 print("niachom")

for i in nud:
   print(i, "\n")

j=0
while j < 10:
   print(j)
#   j-=1
   j+=1


arry = [32323,545445,232535,["no,d",3,3434.4344,[{"wew": "uyuyuuyu"}]]]
cort = ("dasdsd",'sdsds',2323)
dict = ({"dict1": "dict value"})
print(dict['dict1'])

plur = {"434","erer"}

def xoxo(stri):
  return stri
xoxo(nud)


lya =  lambda x, y: print(x - y)
lya(int(nud), float(nud))
