
from ntpath import join
import time


#Function to find partition position
def partition(array,low,high):
    
    #Choosing the rightmost(end) element as pivot
    pivot = array[high]

    #pointer for greater element
    i = low-1

    #traverse through all the elements
    #compare each element with pivot.
    for j in range(low,high):
        if array[j] <= pivot:
            #if element is smaller than pivot, swap it with the greater element pointed by i
            i=i+1
            #swapping element at i with element at j
            (array[i],array[j]) = (array[j],array[i])

    #swap the pivot element with the greater element specified by i
    (array[i+1],array[high])=(array[high],array[i+1])
    #return the position from where partition is done
    return i+1

#Function to perform quicksort
def quickSort(array,low,high):
    if low<high:

        #find pivot element such that element smaller than pivot on left and greater on right
        part_id=partition(array,low,high)

        #recursive call on the left of pivot
        quickSort(array,low,part_id - 1)
        #recursive call on the right of pivot
        quickSort(array,part_id +1,high)



#create an array to store words
word_list=[]
#open the text file containing word data and read
with open('wordlist.txt') as f:
    word_list=f.readlines()
f.close()

#get the size of array
size=len(word_list)

#using the time library to get the start time.
start_time=time.time()

#calling the quicksort function
quickSort(word_list,0,size-1)

#get the end time
end_time=time.time()

#create a text file to store the sorted word list
with open('sorted.txt','w') as output_file:
    for line in word_list:
        output_file.write("".join(line))
output_file.close()


#print the elapsed time
print('The time elapsed is:',(end_time-start_time)*1000,' milliseconds')
print('The sorting process has complete. sorted.txt has been created')

