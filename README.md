Electron-Cutout-Factors
=======================

Dependencies
------------

On Windows 7 64-bit I installed the following:

* [Anaconda3 64-bit](http://continuum.io/downloads#py34)
* [pywin32 64-bt](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win-amd64-py3.4.exe/download)
* [pandoc](https://github.com/jgm/pandoc/releases)
* [node.js](http://nodejs.org/)


Running the code
----------------

Edit the desired parameters within the csv file: <br>
`input/parameters.csv`

Place input tables in csv format for each applicator and energy within the directory: <br>
`input/data/`

-Note: first row of these input files are not read by the program. It is expected that "width, length, and factor" will be written there.


Execute: <br>
`runmodel.py`



Reviewing the results
---------------------

The output data and respective reports can be found within: <br>
`output/YYYYmmdd_HHMMSS`
