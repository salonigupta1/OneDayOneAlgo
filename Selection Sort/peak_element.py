# -*- coding: utf-8 -*-
"""peak_element.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f4f4hb5QIOEJANOnEfnj05tc328ioEwX
"""

#a code to find any peak element in a given array
#peak element is the element which is greater than it's neighbouring elements
#the logic is to sort array and print last element of the array
arr=[1,2,43,2,76,89,32,4555,101,45,32]
for first_elem in range(0,len(arr)-1,1):
  for remain_elem in range(first_elem+1,len(arr)):   #reserving first element and iterating through remaining list
    if arr[first_elem]>arr[remain_elem]:  #if remaining list has element smaller than first element,replace
      arr[first_elem],arr[remain_elem]=arr[remain_elem],arr[first_elem]
print("The peak element is {}".format(arr[-1]))  #print the last element