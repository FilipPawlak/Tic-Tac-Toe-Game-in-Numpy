#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 18:18:32 2020

@author: filippawlak
"""

import numpy as np

# Plansza początkowa
plansza = np.empty((3,3,), dtype='U')
plansza[:] = "^"
liczby = np.array([1,2,3,4,5,6,7,8,9], dtype='U').reshape(3,3)

slownik = {1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1], 9:[2,2]}

def liczba():
    x = input()
    if x not in ['0','1','2','3','4','5','6','7','8','9']:
        print ('Zmień dilera. Jaki jest Twój ruch?')
        wynikx = liczba()   
    else:
       wynikx = int(x) 
    return wynikx
        
                

def zmianaX (i):   
    plansza[slownik[i][0],slownik[i][1]] = 'X'

def zmianaO (i):   
    plansza[slownik[i][0],slownik[i][1]] = 'O'


def gracz (k):
    if k%2 == 0:
        gracz = gracz1
    else:
        gracz = gracz2
    return gracz


def silnik (wybor):
    if plansza[slownik[wybor][0],slownik[wybor][1]] != '^':
        print('To pole jest już zajęte!')
        b = liczba()
        silnik(b)
    else:
        if a==gracz1:
            zmianaX(wybor)
        else:
            zmianaO(wybor)
  
def konwersja (plansza):
    plansza2 = plansza.copy()
    plansza2[plansza2 == 'X' ] = 1
    plansza2[plansza2 == 'O' ] = 0
    plansza2[plansza2 == '^' ] = 99
    return plansza2

    
    

def sprawdzenie (plansza2):
    wynik = []
    z=0
    for i in np.sum(plansza2, axis = 1): wynik.append(i)
    for i in np.sum(plansza2, axis = 0): wynik.append(i)
    np.sum(np.diag(plansza2))
    np.sum(np.diag(np.fliplr(plansza2)))
    for i in wynik: 
        if i in [0,3]:
            z=z+1
    return z
    
        

        
        
# silnik gry
print('Podaj imię pierwszego gracza:')
gracz1 = input()
print('Podaj imię drugiego gracza:')
gracz2 = input()
wybor = 1
runda = 1
k = 1
while wybor:
    runda = runda + 1
    l = runda//2
    k = k + 1
    print('\n******************************************************************\n', end = '')
    print(f"Runda: {l}")
    a = gracz(k)
    print(f"Gracz: {a}")
    print('\nGra:')
    print(plansza)
    print(f'\n{a},Twój ruch:')
    print(liczby)
    wybor = liczba()
    if wybor == 0:
        break
    else:
        silnik(wybor)
        plansza2 = konwersja(plansza)
        plansza2 = np.array(plansza2).astype(int)
        if sprawdzenie(plansza2) > 0:
            print(f'Koniec gry. Zwyciężył gracz {a} ')
            break
        elif '^' not in plansza.flatten().tolist():
            print('\nRemis!!!')
            break
        else:
            continue
    
    


