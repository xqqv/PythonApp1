from random import *
from math import * 
""" #6
try:
    aeg = float(input("Mitu tundi kulus sõiduks? "))
    try:
        teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
        kiirus = teepikkus/aeg
        print("Sinu kiirus oli " + str(kiirus) + " km/h")
    except :
        print("Viga andmetaga!")
except :
    print("on vaja ainult numbrid sisestada!")
"""


"""
print("Sinu kiirus oli " + str(kiirus) + " km/h")

#5
a=float(input("pikkus: "))
b=float(input("Laius: "))
d=sqrt(a**2+b**2)
print("Diagonaal=",d, "m")


#4
u=float(input("ümbermõõt: ")
d=round(u/pi,2)
d=round(u/pi,2)
print("Läbimõõt =".d)
"""

#7

"""
num1 = int(input("Sisestage esimene täisarv "))
num2 = int(input("Sisestage teine ​​täisarv "))
num3 = int(input("Sisestage kolmas täisarv"))
num4 = int(input("Sisestage neljas täisarv"))
num5 = int(input("Sisestage viies täisarv"))

average = (num1 + num2 + num3 + num4 + num5) / 5
print("Sisestatud arvude aritmeetiline keskmine:", average)

 #(teise variant)
try:
    min_=int(input("Min: ":))
except :
    print("On vaja täisarv kasutada!")
try:
    max_=int(input("Max: "))
except :
    print("Viga max_ muutujaga!")
 

#8

print("   @..@")
print("   (----)")
print("  ( \\__/ )")
print("^^ \"\" ^^")

#9 """

a = int(input("Sisesta esimese külje pikkus: "))
b = int(input("Sisesta teise külje pikkus: "))
c = int(input("Sisesta kolmanda külje pikkus: "))
umbermoot = a + b + c
print(a+b+c)

#10 
pizza_cost = 12.90
tip_percentage = 10

num_people = int(input("Kui palju inimesi tellib pitsat? "))

tip_amount = pizza_cost * (tip_percentage / 100)
total_cost = pizza_cost + tip_amount
cost_per_person = total_cost / num_people


print("\nPitsa hind:", pizza_cost, "euro")
print("tip",tip_percentage, "%):", "{:.2f}".format(tip_amount), "euro")
print("kogumaksumus:", "{:.2f}".format(total_cost), "euro")
print("\nKõik peavad maksma:", "{:.2f}".format(cost_per_person), "euro")
