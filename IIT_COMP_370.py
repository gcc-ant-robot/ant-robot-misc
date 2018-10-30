from PIL import Image, ImageDraw
import os, re

X_SCALE_GUESS = 10
Y_SCALE_GUESS = 5

truthfile = os.getcwd() + "\\Groundtruth.txt"

truth = []
for line in open(truthfile):
    tup = line.rstrip('\n').split('i')
    truth.append(tup)

# Parse results files
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

results = []
for i in range(5,len(rowVals)-2):
    results.append([int(rowVals[i])*X_SCALE_GUESS, int(colVals[i])*5]*Y_SCALE_GUESS)
    

# Get all files in directory
i=0
for filename in os.listdir(os.getcwd()):
    if(filename.endswith(".jpg")):
        center = results[i]
        fp = open(filename, "rb")
        im = Image.open(fp)
        draw = ImageDraw.Draw(im)
        draw.rectangle([(center[0]-5,center[1]-5),(center[0]+5,center[1]+5)],width=2, outline = "red");
        im.save(os.getcwd()+"\\results\\"+filename, "JPEG")
        i+=1
