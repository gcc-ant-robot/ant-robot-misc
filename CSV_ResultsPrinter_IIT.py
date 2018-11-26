import os, re, csv

#Set scaling factor used in IIT
X_SCALE = 7
Y_SCALE = 7

#Parse ground truth file
truthfile = os.getcwd() + "\\images\Groundtruth.txt"

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
    pred.append([int(rowVals[i])*X_SCALE, int(colVals[i])*Y_SCALE])
    
# Prepare data for printing to csv
results = [['%IIT Algorithm'],['%video'],['%other'],['frameid','truex','truey','predx','predy']]
for i in range(0,len(actual)):
    tup = [i] + actual[i] + pred[i]
    results.append(tup)
    
# Print to csv
fileName = os.getcwd() + "\\results\\results.csv"
with open(fileName , "w", newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(results)



    
