#Blayne Hoy
#U2 Lab2

import ctypes
import colorama


class DynamicArray:

    def __init__(self):
        self.__n = 0
        self.__capacity = 1
        self.__A = DynamicArray.__make_array (self, self.__capacity)

    
    def append(self, ele):
        if self.__n == self.__capacity:
            self.__resize(2 * self.__capacity)  
        self.__A[self.__n] = ele
        self.__n += 1

    
    def __resize(self, c):
        self.__capacity += self.__capacity
        temparray = DynamicArray.__make_array(self, self.__capacity)
        for x in range(self.__n):
            temparray[x] = self.__A[x]
        
        self.__A = temparray


    
    def get_cap(self):
        return(self.__capacity)

    def __len__(self):
        return self.__n


    def __str__(self):
        if self.__n == 0:
            return "[]"

        out = '['
        for i, element in enumerate(self.__A):
            try:
                out += str(element) + ', '
                temp = self.__A[i+1]
            except:
                break
        return out[:-2] + ']'

    def __getitem__(self, k):
        """return element at index"""
        if k <= 0 or k >= self.__n:
            raise IndexError("invalid index")
    
        return self.__A[k]

    def __make_array(self, c):
        """return new array with capacity c"""
        return (c * ctypes.py_object)()