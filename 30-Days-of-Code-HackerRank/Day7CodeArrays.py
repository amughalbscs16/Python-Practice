
#Task
#Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.
import sys

newarray=[]
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(len(arr)):
    print(arr[len(arr)-i-1],end=" ")


#Sample Input
#4
#1 4 3 2
#Sample Output
#2 3 4 1