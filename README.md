Electron-Cutout-Factors
=======================

Dependencies
------------

On Windows 7 64-bit I installed the following:

* [Anaconda3 64-bit](http://continuum.io/downloads#py34)
* [pywin32 64-bt](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win-amd64-py3.4.exe/download)
* [pandoc](https://github.com/jgm/pandoc/releases)
* [node.js](http://nodejs.org/)


Running the model
-----------------

Edit the desired parameters within the csv file:

    input/parameters.csv

Place input tables in csv format for each applicator and energy within the directory:

    input/data/



Execute:

    runmodel.py



Reviewing the results
---------------------

The output data and respective reports can be found within:

    output/YYYYmmdd_HHMMSS
