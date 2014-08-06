Electron Cutout Factors
=======================

For the modelling of electron cut-out factors in Radiation Oncology Medical Physics.



Dependencies
------------

On Windows 7 64-bit I installed the following:

* [Anaconda3 64-bit](http://continuum.io/downloads#py34)
* [pywin32 64-bt](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win-amd64-py3.4.exe/download)
* [pandoc](https://github.com/jgm/pandoc/releases)
* [node.js](http://nodejs.org/)


User parameters
---------------

Edit the desired parameters within the csv file:

    input/parameters.csv

The parameters available for editing are the following:

 * `gapThreshold` — The cutoff for the gap parameter
 * `giveThreshold` — the cutoff for the give parameter
 * `figureElev` — The elevation of the 3D plots within the reports
 * `figureAzim` — The rotation of the 3D plots within the reports
 * `widthInterpResolution` — The number of values along the width axis to be outputted in the interpolation table
 * `ratioInterpResolution` — The number of values along the ratio axis to be outputted in the interpolation table


Input data
----------

Place input tables in **csv** format for each applicator and energy within the directory:

    input/data/
    
The width parameter (minor axis) is less than or equal to the length parameter (major axis) of the cut-out shape. These lengths and widths can be defined at either 95 cm or 100 cm SSD as long as the use is consistent.

The model will be run for every file csv file within this directory. In order to speed up modelling archive the data files that are not currently being used.


Requested cutouts
-----------------

Place a csv table of requested cutouts within the directory:

    input/requested-cutouts/
    
Note: the filename of these requested cutouts must be the same as the corresponding data file given in `input/data/`.


Running the model
-----------------

Execute:

    runmodel.py



Reviewing the results
---------------------

The output data and respective reports can be found within:

    output/YYYYmmdd_HHMMSS/
    

This data is divided into folders according to the `input/data/` filename. Within each output folder the following is found:

 * `*_report.html` — A printout of the model code that was run for this data set.
 * `interpolation-table.csv` — A printout of the interpolation table with the width and ratio resolutions defined in `input/parameters.csv`.
 * `predicted-cutouts.csv` — A printout of the predicted cutouts that were requested within the corresponding csv file in `input/requested-cutouts/`. This only appears if cutout factors were requested. A factor is left blank if either the give or the gap parameters were above the threshold values defined in `input/parameters.csv`.



No warranty
----------
BECAUSE THE PROGRAM IS LICENSED FREE OF CHARGE, THERE IS NO WARRANTY
FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT WHEN
OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES
PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED
OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.  THE ENTIRE RISK AS
TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.  SHOULD THE
PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING,
REPAIR OR CORRECTION.
