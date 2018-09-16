# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 21:22:22 2018

@author: Jose Carlos Vega

"""
f=open ("entrenamiento.txt")
data = f.read().strip()
f.close

m=[[int(num) for num in line.strip().split()]for line in data.split('\n')]
print (m)
print (len(m))
print (len(m[0]))
print ("\n")
for x in range(0,len(m[0]) ):
    print(m[0][x])
    
print("Vector interior: " ,m[0])
matriz = m[0][2]

print("dato interior:",matriz)
nuevo = [i for i in range(10)]
for i in range(0,5):
    nuevo[i]=i+1

print("se tiene: ",nuevo)

a={1,2,3,4,5}
b={1,2,3,4,5,6}
tetha = [i for i in range(len(m[0]))]
for i in range(0,len(m[0])):
    tetha [i] =0
print(tetha)

def h(x,t):
    suma=0
    for i in range(0,len(t)):
        if i==0:
            sumatoria = sumatoria +b[i]
        else:
            sumatoria = sumatoria + a[i-1]*b[i]
        return sumatoria

def funcioncosto(x,tt):
    resultado = 0.00
    for i in range(0,len(x)):
        res=[i for i in range(len(x[0])-1)]
        for j in range(0,len(x[0])-1):
            res[j] = x[i][j]
            resultado = resultado + pow(h(res,tt)-1[i][len(x[0])-1],2)
            resultado = resultado/(len(m)*2)
            return resultado