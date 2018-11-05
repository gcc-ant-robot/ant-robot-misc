import os, re, csv

X_SCALE_GUESS = 1
Y_SCALE_GUESS = 1


#Parse ground truth file
truthfile = os.getcwd() + "\\Groundtruth.txt"

truthRect = []
for line in open(truthfile):
    tup = [int(x) for x in line.rstrip('\n').split(',')]
    truthRect.append(tup)

# Turn rectangles into center point truth
actual = []
for coords in truthRect:
    tup = [int(coords[0] + coords[2]/2), int(coords[1] + coords[3]/2)]
    actual.append(tup)
    

# Parse results files of IIT
rowFile = os.getcwd() + "\\results\TargetLocationRow"
colFile = os.getcwd() + "\\results\TargetLocationCol"

rowVals = []
for line in open(rowFile):
    rowVal = line.rstrip().lstrip()
    rowVals.append(rowVal)

colVals = []
for line in open(colFile):
    colVal = line.rstrip().lstrip()
    colVals.append(colVal)

pred = []
for i in range(5,len(rowVals)-2):
    pred.append([int(rowVals[i])*X_SCALE_GUESS, int(colVals[i])*Y_SCALE_GUESS])
    
# Prepare data for printing to csv
results = [['frameid','truex','truey','predx','predy']]
for i in range(0,len(actual)):
    tup = [i] + actual[i] + pred[i]
    results.append(tup)

#Print to csv
fileName = os.getcwd() + "\\results\\results.csv"
csvFile = open(fileName , "w", newline='')
writer = csv.writer(csvFile)
writer.writerows(results)



    
