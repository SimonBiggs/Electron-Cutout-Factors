Electron-Cutout-Factors
=======================

For the modelling of electron cut-out factors in Medical Physics.



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

Place a table of requested cutouts within the directory (the filename must match the data set):

    input/requested-cutouts/
    




Execute:

    runmodel.py



Reviewing the results
---------------------

The output data and respective reports can be found within:

    output/YYYYmmdd_HHMMSS/
    

This data is divided into folders according to the `input/data/` filename. Within each output folder a report of the code is given along with an interpolation table and the requested cut-out data.
