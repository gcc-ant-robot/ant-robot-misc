import csv
import os, pathlib, sys
import pandas as pd
import matplotlib.pyplot as plt

# CSV must follow the format: frameid,truex,truey,predx,predy
def readData(csv_filename):
    file = open(csv_filename, "r")

    # Read extra header lines
    algorithm = file.readline().strip()[1:]
    videoId = file.readline().strip()[1:]
    desc = file.readline().strip()[1:]

    # Open the results
    data = pd.read_csv(file)
    # Calculate Error
    data["L1"] = data.apply(lambda row: L1Distance(row), axis=1)
    data["L2"] = data.apply(lambda row: L2Distance(row), axis=1)
    data["algorithm"] = data.apply(lambda row: algorithm, axis=1)
    data["video"] = data.apply(lambda row: videoId, axis=1)
    file.close()
    return data

def L1Distance(row):
    return abs(row['truex'] - row['predx']) + abs(row['truey'] - row['predy'])

def L2Distance(row):
    return pow(row['truex'] - row['predx'],2) + pow(row['truey'] - row['predy'],2)

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Please provide path to results folder as an argument")
        sys.exit(0)
    # open the folder
    folder = sys.argv[1]
    p = pathlib.Path(folder)

    # Read in all the data
    frames = []
    for file in p.iterdir():
        if(file.suffix == ".csv" and not file.name.endswith("Summary.csv")):
            f = readData(file)
            frames.append(f)
    data = pd.concat(frames)

    # Make figure with all the time plots
    videoNames = data["video"].unique()
    algorithmNames = data["algorithm"].unique()

    # Generate Boxplots
    data.boxplot(column=['L1'], by='algorithm')
    plt.title("L1 Error")
    plt.suptitle("")
    plt.savefig(p.name + "/" + "boxplot.jpg", dpi=150)

    # Generate Error over time figure
    for row, video in enumerate(videoNames):
        # Define subplot and plot it
        fig, ax = plt.subplots(figsize=(8,6))
        data.loc[(data["video"] == video)].groupby(["algorithm"])["L1"].plot( x="time",y="L1 Error",title=video, legend=True)
        plt.xlabel("time")
        plt.ylabel("L1 error")
        plt.savefig(p.name + "/" + video + ".jpg", dpi=150)


    for algo in algorithmNames:
        summary = data.loc[data["algorithm"] == algo]["L1"].describe()
        summary.to_csv(p.name + "/" + algo + "_Summary.csv")
