Electron Cutout Factors
=======================

For the modelling of electron cut-out factors in Radiation Oncology Medical Physics.



Dependencies
------------

On Windows 7 64-bit I installed the following:

 * [Anaconda3 64-bit](http://repo.continuum.io/anaconda3/Anaconda3-2.0.1-Windows-x86_64.exe)
 * [pywin32 64-bt](http://sourceforge.net/projects/pywin32/files/pywin32/Build%20219/pywin32-219.win-amd64-py3.4.exe/download)
 * [pandoc](https://github.com/jgm/pandoc/releases/download/1.12.4.2/pandoc-1.12.4.2-1-windows.msi)
 * [node.js](http://nodejs.org/dist/v0.10.30/x64/node-v0.10.30-x64.msi)

Recommended Programs
--------------------

 * [Libre Office](http://donate.libreoffice.org/home/dl/win-x86/4.3.0/en-US/LibreOffice_4.3.0_Win_x86.msi) — Works in a less confusing manner with csv files than Microsoft Excel
 * [Google Chrome](https://www.google.com/intl/en-AU/chrome/browser/) — The html reports have an improved display in Google Chrome as opposed to Internet Explorer


On Ubuntu 14.04 64-bit I installed the following:
`sudo apt-get install python3-numpy python3-matplotlib ipython3 ipython ipython3-notebook python3-pandas python3-nose python-pgm python-zmq python3-pip pandoc nodejs libatlas-base-dev gfortran python3-dev build-essential`

`sudo pip3 install runipy`
`sudo pip3 install scipy`



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
    
For each cutout a length, width, and factor needs to be inputted. These lengths and widths can be defined at either 95 cm or 100 cm SSD as long as the use is consistent.

The model will be run for every file csv file within this directory. In order to speed up modelling archive the data files that are not currently being used.


Requested cutouts
-----------------

Place a csv table of requested cutouts within the directory:

    input/requested-cutouts/
    
Note: the filename of these requested cutouts must be the same as the corresponding data file given in `input/data/`.


Running the model
-----------------

On Windows Execute:

    runmodel.py

On Ubuntu run the following in the main directory (`Electron-Cutout-Factors`):

    `ipython3 ./runmodel.py`



Reviewing the results
---------------------

The output data and respective reports can be found within:

    output/YYYYmmdd_HHMMSS/
    

This data is divided into folders according to the `input/data/` filename. Within each output folder the following is found:

 * `*_report.html` — A printout of the model code that was run for this data set. An example can be found [here](http://simonbiggs.net/10app06eng_report).
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
