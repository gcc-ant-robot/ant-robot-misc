import csv, sys

def getGroundTruth(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f, skipinitialspace=True)
        header = ['xmax', 'ymax', 'xmin', 'ymin', 'frameId']
        data = {k:[] for k in header}
        for row in reader:
            for i, col in enumerate(header):
                data[col].append(row[i])
    return data

def saveResults(center, ground_truth, video_name):
    filename = "baseline_" + video_name + ".csv"
    with open(filename, "w") as f:
        f.write("%%baseline\n")
        f.write("%%{}\n".format(video_name))
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['frameid', 'truex', 'truey', 'predx', 'predy'])
        for i, frameId in enumerate(ground_truth['frameId']):
            trueCenter = getCenterFromGroundTruth(i, ground_truth)
            csv_writer.writerow([frameId, trueCenter[0], trueCenter[1], center[0], center[1]])
    print("Saved to {}".format(filename))

def getCenterFromGroundTruth(i, ground_truth):
    x = (float(ground_truth['xmax'][i]) + float(ground_truth['xmin'][i])) / 2
    y = (float(ground_truth['ymax'][i]) + float(ground_truth['ymin'][i])) / 2
    return (x, y)




if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a groundtruth all bounding boxes file path")
        sys.exit(0)
    
    ground_truth = getGroundTruth(sys.argv[1])
    
    center = getCenterFromGroundTruth(0, ground_truth)

    video_name = "".join(sys.argv[1].split(".")[:-1])
    saveResults(center, ground_truth, video_name)




    