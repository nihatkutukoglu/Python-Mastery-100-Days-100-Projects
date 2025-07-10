# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 18:03:15 2025

@author: user
"""
import time 

start = int(input("bir değer giriniz"))

print("\n--- SAYIM BAŞLIYOR ---")

while start > 0 :
    print(start)
    time.sleep(1)
    start -= 1
    
print("\nsayım tamamlandı")