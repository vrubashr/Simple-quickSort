
from ntpath import join
import time

start_time=time.time()

def partition(array,low,high):
    pivot = array[high]
    i = low-1

    for j in range(low,high):
        if array[j] <= pivot:
            i=i+1
            (array[i],array[j]) = (array[j],array[i])

    (array[i+1],array[high])=(array[high],array[i+1])

    return i+1


def quickSort(array,low,high):
    if low<high:

        part_id=partition(array,low,high)

        quickSort(array,low,part_id - 1)

        quickSort(array,part_id +1,high)


word_list=[]
with open('wordlist.txt') as f:
    word_list=f.readlines()

size=len(word_list)
quickSort(word_list,0,size-1)

with open('sorted.txt','w') as output_file:
    for line in word_list:
        output_file.write("".join(line))
output_file.close()

end_time=time.time()

print('The sorting process has complete. sorted.txt has been created')
print('The time elapsed is:',(end_time-start_time),' seconds')
