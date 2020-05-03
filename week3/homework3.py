import numpy as np
import random

def arr_replace(arr):
    arr = np.array(arr)
    arr[arr%2!=0]=0
    return arr


def arr_replace_where(arr):
    return np.where(arr%2 == 0,0,arr)


def arr_repeat(arr):
    arr=np.array(arr)
    return arr.repeat(3)


def arr_join(arr1):
    return np.concatenate((arr1,arr1,arr1))


def arr_intersection(arr1,arr2):
    arr1=np.array(arr1)
    arr2=np.array(arr2)
    return np.intersect1d(arr1,arr2)


def arr_random():
    a=np.random.randint(5,10,(2,2))
    b=np.random.rand(2,2)
    return np.around(np.array(a+b),2)


