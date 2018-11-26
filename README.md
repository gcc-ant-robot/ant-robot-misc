# ant-robot-misc
A repository for storing miscellaneous scripts and tools for the ant robot research

# Dependencies
The following packages are needed to run the data summary scripts
- `pandas`
- `matplotlib`

# Results csv format

Filename: `<algorithm>_<video>_results.csv`

	%algorithm
	%video
	%other
	frameid,truex,truey,predx,predy
	...

# Scripts

## processResults.py
This script will process a folder of result files formatted as described above.
It generates
* summary files for each algorithm
* a boxplot comparing the algorithms error
* a figure showing the error over time for all algorithms and videos

Uses Python 3

### Example
Given a folder with results:

	folder
		results1.csv
		results2.csv
		...

Use `python processResults.py folder`

## CSV_ImagePrinter.py
This script will use a results.csv file (in the above format) to print bounding boxes on a set of images.
The configuration requires:
* File exists ".\results\results.csv"
* Images to print boxes on are in ".\images\"

New images will be created in ".\results" with a 10x10 box centered on (truex, truey) in blue and centered on (predx, predy) in red.

## CSV_ResultsPrinter_IIT.py
This script will create the results.csv from the IIT Algorithm's output.
The configuration requires:
* X_SCALE and Y_SCALE parameters should be set to the int ceil(image_width/hor_FOV) (e.g. for a 340x240 picture with a 50deg FOV, ceil(340/50) = 7)
* STNS Dataset GroundTruth.txt is located at "\images\Groundtruth.txt"
* IIT files exist at ".\results\TargetLocationCol" and ".\results\TargetLocationRow"
Output is ".\results\\results.csv"
