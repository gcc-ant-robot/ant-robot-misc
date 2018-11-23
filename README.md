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

## CSV_ImagePointer_COMP370.py

## CSV_Results_COMP370.py

## IIT_COMP_370.py
