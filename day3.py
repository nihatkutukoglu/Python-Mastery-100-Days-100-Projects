# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 00:23:40 2025

@author: user
"""


#  Basit hesap makinesi 
num1 = float(input("1. sayının değerini girin"))
num2 = float(input("2.sayıyı girin"))

toplama = num1+num2 
çıkarma = num1-num2
çarpma = num1*num2
bölme = num1/num2 if num2!= 0 else "sıfıra bölünmez"

print("\n Hesap sonucları" )
print(f"toplama = {num1} + {num2} = {toplama}")
print(f"çıkarma = {num1} - {num2} = {çıkarma}")
print(f"çarpma = {num1} * {num2} = {çıkarma}")
print(f"bölme = {num1} / {num2} = {bölme}")

