# The hisotorians can't agree on how to read the chief's handwriting
# but a lot of location ID's appear in both lists!
# Maybe the other numbers aren't location ID's at all, but misinterpreted handwriting


#figure out exactly how often each number in list 1 appears in list 2
#calculate a total similarity score by adding up each number in list 1 after multiplying
#  it by the number of times that then umber appears in list 2

#import some things
import numpy as np

#load the data
#data = np.loadtxt('sampleinputDay1.txt', dtype = float)
data = np.loadtxt('inputDay1.txt', dtype = float)

#iterate down the first column and find the number of times that number appears in the second column
count = 0
for i in data[:,0]:
    srch = data[:,1] == i
    #similarity score:
    # multiply the number in col1 by number of times it appears in col2 and add to count
    count = count + np.sum(srch) * i
    

#print similarity score
print('the similarity score is: ', count)


