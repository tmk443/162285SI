import numpy as np
import math
import random

def symbole_klas_decyzyjnych(file): # zadanie 3a
    return unikalne_wartosci_dla_kolumny(file, len(file[0])-1)

def wielosc_klas_decyzyjnych(file): # zadanie 3b
    return unikalne_wartosci_dla_kolumny(file, len(file[0])-1)

def min_max(file,file2):  # zadanie 3c
    temp_list = np.empty(len(file2),dtype=object)
    for x in range (0 , len(file2 )) :
        temp_list[x] = file2[x][1]
    temp_min_max = [ [0]*2 for i in range(6)]
    iter = 0
    for x in range(0,len(temp_list)):
        temp_column = np.empty([len(file)],dtype=float)
        iter2=0
        if(temp_list[x] == 'n'):
            for row in file:
                temp_column[iter2]=(row[x])
                iter2=iter2+1
            for x in range(0,len(temp_column)):
                temp_column[x] = float(temp_column[x])
            temp_min_max[iter][0] = min(temp_column)
            temp_min_max[iter][1] = max(temp_column)
            iter = iter+1
    return temp_min_max

def liczba_unikalnych_wartosci(file): # zadanie 3d
    temp = []
    for x in range(len(file[0])-1):
        temp.append( len(unikalne_wartosci_dla_kolumny(file, x)))
    return temp

def unikalne_warosci2(file): # zadanie 3e
    temp = []
    for x in range(len(file[0])-1):
        temp.append(unikalne_wartosci_dla_kolumny(file, x))
    return temp

def unikalne_wartosci_dla_kolumny(file, column): # pomocnicza funkcja
    temp = []
    for x in file:
        temp_element = x[column]
        if temp_element not in temp:
            temp.append(temp_element)
    return temp

def odchylenie(file, file2): # zadanie 3f
    temp_list = np.empty(len(file2),dtype=object)
    for x in range (0 , len(file2 )) :
        temp_list[x] = file2[x][1]
    iter = 0
    for x in range(0,len(temp_list)):
        temp_column = np.empty([len(file)],dtype=float)
        iter2=0
        if(temp_list[x] == 'n'):
            for row in file:
                temp_column[iter2]=(row[x])
                iter2=iter2+1
            for x in range(0,len(temp_column)):
                temp_column[x] = float(temp_column[x])
            iter = iter+1
            print(np.std(temp_column, dtype=np.float64))

def najczesciej_wystepujaca_wartosc_dla_kolumny(file, column): # zadanie 4a pomocnicza
    unikalne = unikalne_wartosci_dla_kolumny(file, column)
    maks_licznik = 0
    maks_wartosc = unikalne[0]
    for y in unikalne:
        wartosc = y
        licznik = 0
        for x in range(len(file)):
            if file[x][column] == wartosc:
                licznik = licznik + 1
        if licznik>maks_licznik:
            maks_licznik = licznik
            maks_wartosc = y
    return maks_wartosc

def uzupelnianie_pytajnikami(file): # zadanie 4a pomocnicza
    row = len(file)
    col = len(file[0])-1
    sum = row*col
    i=0
    while i < int(sum)//10:
        first = random.randint(0,row-1)
        second = random.randint(0,col-1)
        if file[first][second] == '?':
            i-=1
        file[first][second]='?'
        i+=1
    return file

def srednia_dla_kolumny(file, column): # zadanie 4a pomocnicza
    suma = 0
    licznik = 0
    for x in range(len(file)):
        suma = suma + float(file[x][column])
        licznik = licznik + 1
    return round((suma/licznik),10)

def uzupelnianie_danych(pierwotny, file,file2): # zadanie 4a
    row = len(file)
    col = len(file[0]) - 1
    for x in range(row):
        for y in range(col):
            if file[x][y] == '?':
                if file2[y][1] == 'n':
                    file[x][y] = srednia_dla_kolumny(pierwotny, y)
                else:
                    file[x][y] = najczesciej_wystepujaca_wartosc_dla_kolumny(pierwotny, y)
    return file

def normalizacja(file, file2,  minmax): #zadanie 4b
    row = len(file)
    col = len(file[0]) - 1
    iter = 0
    for x in range(row):
        iter = 0
        for y in range(col):
            file[x][y] = float(file[x][y])
            if file2[y][1] == 'n':
                file[x][y] = round((file[x][y] - minmax[iter][0] * (0 - 1)) / (minmax[iter][1] - minmax[iter][0]),5)
                iter = iter + 1
    return file

def standaryzacja(file, file2): # zadanie 4c
    row = len(file)
    col = len(file[0]) - 1
    for x in range(row):
        for y in range(col):
            mean = srednia_dla_kolumny(file, y)
            variance = sum(pow(a - mean, 2) for a in range(y))
            file[x][y] = float(file[x][y])
            if file2[y][1] == 'n':
                file[x][y] = (file[x][y] - mean)/variance
    return file


australian1 = np.loadtxt("dane/australian.txt", dtype=object)
australian1Copy=np.copy(australian1)
australian2 = np.loadtxt("dane/australian-type.txt", dtype=object)

print(symbole_klas_decyzyjnych(australian1))        # zadanie 3a
print(wielosc_klas_decyzyjnych(australian1))        # zadanie 3b
print(min_max(australian1, australian2))            # zadanie 3c
print(liczba_unikalnych_wartosci(australian1))      # zadanie 3d
print(unikalne_warosci2(australian1))               # zadanie 3a
print(odchylenie(australian1, australian2))         # zadanie 3f
uzupelnianie_danych(australian1, australian1Copy, australian2)  # zadanie 4a
print(normalizacja(australian1, australian2, min_max(australian1, australian2)))  # zadanie 4b
print(standaryzacja(australian1, australian2))      # zadanie 4c



