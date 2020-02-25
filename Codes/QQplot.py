# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 21:42:58 2020

@author: Admin
"""


import time
start_time = time.time()
for i in range(0,5):
    
    print(i)
    time.sleep(5)
endtime = time.time()

print(endtime-start_time)   



a = ['adsfasdfasdfasdf']
b = a.copy()
for i in range(0,3):
    b[0] = 'alay ' + b[0]
    for i in range(0,4):
        print(b)
    b = a.copy()
    print(b)




a= [1,2,3,4]
b = a
b.append(5)
print(a)
print(b)

b =a.copy()

b.append(7)
a
b




def test():
    a =7
    b = 5 +a
    print(a)
    
test()
