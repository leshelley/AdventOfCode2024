# the engineers forgot to tell you about the problem dampener!

# the reactor safety system tolerates a signle bad level if would otherwise be a safe report
# so removing a single level from an unsafe report would make it safe


#initialize some things
import numpy as np
safe = []
linecount = 0 #line counter for safe var

#load input data
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

        #check if removing a level would make the report safe
        for i in range(len(reportTmp)):
            reportTmp2 = np.delete(reportTmp, i)
            diffScoresTmp2 = np.diff(reportTmp2)

            #check if all pos or all neg
            sameSignTmp2 = np.all(diffScoresTmp2 > 0) | np.all(diffScoresTmp2 < 0) #true = safe

            #check if gradual increase
            gradualTmp2 = np.all(abs(diffScoresTmp2) >= 1) and np.all(abs(diffScoresTmp2) <= 3) #true if safe

            #if both are true, mark as safe, else remains as is
            if sameSignTmp2 and gradualTmp2:
                safe[linecount] = 1
        linecount = linecount + 1



print('with the problem dampener, the number of safe reports is ', sum(safe))
