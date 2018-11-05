from PIL import Image, ImageDraw
import os, re, csv

X_SCALE_GUESS = 1
Y_SCALE_GUESS = 1

#Parse ground truth file
fileName = os.getcwd() + "\\results\\results.csv"
csvFile = open(fileName, 'r')
reader = csv.reader(csvFile)

next(reader) # skip header

results=[]
for row in reader:
    results.append([int(x) for x in row])

#Fix scaling factor in algorithm's results
for i in range(0,len(results)):
    results[i][3] *= X_SCALE_GUESS
    results[i][4] *= Y_SCALE_GUESS 

# Draw rectangles on images and save to new directory
i=0
for filename in os.listdir(os.getcwd()):
    if(filename.endswith(".jpg")):
        coords = results[i]
        fp = open(filename, "rb")
        im = Image.open(fp)
        draw = ImageDraw.Draw(im)
        draw.rectangle([(coords[1]-5,coords[2]-5),(coords[1]+5,coords[2]+5)],width=2, outline = "blue");
        draw.rectangle([(coords[3]-5,coords[4]-5),(coords[3]+5,coords[4]+5)],width=2, outline = "red");
        im.save(os.getcwd()+"\\results\\"+filename, "JPEG")
        i+=1
