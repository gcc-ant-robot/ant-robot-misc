import csv
import pandas as pd
import matplotlib.pyplot as plt

# CSV must follow the format: frameid,truex,truey,predx,predy
def readData(csv_filename, results_filename, l1_plot_name,l2_plot_name):
    # Open the results
    data = pd.read_csv(csv_filename)

    # Calculate statistics
    data["L1"] = data.apply(lambda row: L1Distance(row), axis=1)
    data["L2"] = data.apply(lambda row: L2Distance(row), axis=1)

    print(data)
    # Output Boxplot
    fig, ax = plt.subplots(figsize=(10,  10))
    data.boxplot(["L1"], ax=ax)
    fig.savefig(l1_plot_name)
    data.boxplot(["L2"], ax=ax)
    fig.savefig(l2_plot_name)

    # Output results
    summary = data[["L1","L2"]].describe()
    summary.transpose().to_csv(results_filename)


def L1Distance(row):
    return abs(row['truex'] - row['predx']) + abs(row['truey'] - row['predy'])

def L2Distance(row):
    return pow(row['truex'] - row['predx'],2) + pow(row['truey'] - row['predy'],2)

readData("results.csv","output.csv","l1.jpg","l2.jpg")
