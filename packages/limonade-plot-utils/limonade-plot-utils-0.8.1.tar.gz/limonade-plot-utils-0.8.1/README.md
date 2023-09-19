# Limonade-plot-utils

Limonade is a library meant to simplify handling of list mode data from different sources. The scripts 
provided in limonade-plot-utils are example scripts on how to plot and sort list-mode data with limonade 
and matplotlib.

Included are:
* **read_list_data:** Load and plot list mode data using specific plot configuration. 
  * By default the data is loaded with the
  setup frozen in the data directory, but different detector configuration can be given.
  * Only part of the data can be plotted by using time-slices.
  * Histograms can be exported to comma separated ASCII-files.
  * Histograms can be exported to .phd files with command line inputs for efficiency calibration files and data 
  collection information. 
* **read_hist_data:** Load and plot comma separated ASCII-files saved with read_list_data. The metadata contains all 
    the necessary information.
* **create-plots:** Create simple plot configurations for a given detector.
* **fix-data:** Experimental. Truncate data to smallest data file length. Used to recover data after daq crash.



## Installation
Install with 

        pip install limonade-plot-utils

preferably using virtual environment or --user flag to prevent any clashes with permissions.

After installation one can make basic plots for a given limonade detector with command

        create-plots det_name

Plot files are then automatically created in limonade config dir.

