# chief historian is missing, he was polanning to go to a bunch of 
# historical sites, found a list of historical sites and the elves 
# compile two lists

import pandas as pd
import numpy as np

#read input data
#data = np.loadtxt('sampleinputDay1.txt')
data = np.loadtxt('inputDay1.txt', dtype=float)

#There's just one problem: by holding the two lists up side by side 
# (your puzzle input), it quickly becomes clear that the lists aren't 
# very similar. Maybe you can help The Historians reconcile their lists?


#split columns into two vectors and sort
col1sorted = np.sort(data[:,0])
col2sorted = np.sort(data[:,1])

#find offset between two columns
offset = sum(abs(col1sorted - col2sorted))


#print offset
#sample input data should print 11
print('The offset between the two columns is: ',offset)






