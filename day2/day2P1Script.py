# first location is the red-nosed reindeer nuclear fusion plant
#no sign of chief historian, but the engineers there ask for help
#analyzing some unusual data from the red-nosed reactor

#the data: each row is a report that contains level readings separated by spaces
#engineers want to know which reports are safe
#reactor can only tolerate levels that are gradually increasing or gradually decreasing

#safe report if both are true:
# 1) the levels are either all increasing or all decreasing
# 2) any two adjacent levels differ by at least 1 and at most 3

#how many reports are safe??

#initialize some things
import numpy as np
safe = []
linecount = 0 #line counter for safe var

# read input data line by line and determine if report is safe
#with open('sampleinputDay2.txt') as file:
with open('inputDay2.txt') as file:
    for line in file:
        safe.append(None) #placeholder to add value at index to empty list
        safe[linecount] = 0 #unsafe until proven safe
        reportTmp = np.array(line.split(), dtype = float) #read text report as float
        diffScoresTmp = np.diff(reportTmp)

        #check if all pos or all neg
        sameSignTmp = np.all(diffScoresTmp > 0) | np.all(diffScoresTmp < 0) #true = safe
    
        #check if gradual increase
        gradualTmp = np.all(abs(diffScoresTmp) >= 1) and np.all(abs(diffScoresTmp) <= 3) #true = safe
    
        #if both true, mark as safe, else remains unsafe
        #if sameSignTmp is True and gradualTmp is True: 
        if sameSignTmp and gradualTmp:
            safe[linecount] = 1
        linecount = linecount + 1

print('the number of safe reports is: ', sum(safe))





