# Areege Chaudhary
# 10197607
# I confirm that this submission is my own work and is consistent with the Queen's regulations on Academic Integrity.

import math

def sToInt(string):
    a = 5381
    for ch in string:
        a = a*33 + ord(ch)
    return a

def readName(file):
    return [word for line in open(file, 'r') for word in line.split()]

def insert(key,array):
    a = sumHashFunc(key) #convert key to integer
    if (array[a] == -1): #if spot is empty, insert key there
        array[a] = key
    else: #use quadratic probing or double hashing
        #quadInsert(key, a, array)
        doubleInsert(key, a, array)
        
def quadInsert(key, a, array):
    comparisons = 1
    c1 = 2
    c2 = 2
    i = 0
    size = len(array)
    val = a #a is the integer key value
    while ((i < size) & (array[val] != -1)):
        comparisons += 1 #adds to comparisons count for checking
        i += 1
        val = int((a + c1*i + c2*(i**2)) % size)
    if (array[val] == -1): #if position is empty, insert there
        array[val] = key
        if (comparisons > 10):
            print("Comparisons: " + str(comparisons))
            quit() #if comparisons done exceed 10, terminate program (for checking)
    else:
        print("insert failed")

def doubleInsert(key, a, array):
    comparisons = 1
    i = 0
    size = len(array)
    val = a #a is the integer key value
    while ((i < size) & (array[val] != -1)):
        comparisons += 1 #adds to comparisons count for checking
        i += 1
        val = (a + i*(doubleHashFunc3(key))) % size #change h''(k) depending on trial
    if (array[val] == -1):
        array[val] = key
        if (comparisons > 10):
            print("Comparisons: " + str(comparisons))
            quit() #if comparisons done exceed 10, terminate program (for checking)
    else:
        print("insert failed")

def doubleHashFunc1(key): #h''(k) 1
    key = key**2
    return key

def doubleHashFunc2(key, size): #h''(k) 2
    s = key % size
    return s

def doubleHashFunc3(key): #h''(k) 3
    s = (key + 31)**2
    return s
        
def sumHashFunc(key): #h'(k) 
    sum = 0
    while key:
        sum = sum*2 + key % 10
        key = key // 10
    sum = sum //70 #value changes depending on trial
    return sum

def main():
    maxS = 0
    names = readName("/Users/areegechaudhary/Desktop/names.txt") 
    array = []
    for index in range(8057): #this determines table size
        array.append(-1)
    for name in names:
        k = sToInt(name) #convert string to int
        sum = sumHashFunc(k) #figures out what the max index value needs to be, 
        if (sum > maxS):   #therefore determining what the table size should be
            maxS = sum
        insert(k, array) #attempts to insert key value into array
    print("Max: " + str(maxS))

main()
