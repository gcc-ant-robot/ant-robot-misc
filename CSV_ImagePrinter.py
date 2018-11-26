from PIL import Image, ImageDraw
import os, re, csv

#File should be placed in directory containing folders \images and \results
#Parse ground truth file
fileName = os.getcwd() + "\\results\\results.csv"
with open(fileName, 'r') as csvFile:
    reader = csv.reader(csvFile)
    next(reader) # skip header
    results=[]
    for row in reader:
        results.append([int(x) for x in row])

# Draw rectangles on images and save to new directory
imgDir = os.getcwd() + "\\results\\"
newImgDir = os.getcwd()+"\\results\\"

i=0
for filename in os.listdir(imgDir):
    if(filename.endswith(".jpg")):
        coords = results[i]
        with open(imgDir + filename, "rb") as fp:
            im = Image.open(fp)
            draw = ImageDraw.Draw(im)
            #Draw ground truth box
            draw.rectangle([(coords[1]-5,coords[2]-5),(coords[1]+5,coords[2]+5)],width=2, outline = "blue");
            #Draw pred box
            draw.rectangle([(coords[3]-5,coords[4]-5),(coords[3]+5,coords[4]+5)],width=2, outline = "red");
            im.save(newImgDir+filename, "JPEG")
            i+=1
