Introduction
============

`sdssDR9findingChart` is a script that allows you to automatically download finding charts from Data Release 9 (DR9) of the Sloan Digital Sky Survey (SDSS).

It has been written without using the [`requests`](http://docs.python-requests.org/ "Requests: HTTP for Humans &mdash; Requests 1.1.0 documentation") module so that it can be run without having the users install additional dependencies.

Usage
=====

You invoke the tool with

    sdssDR9findingChart fileWithAstroObjects

where `fileWithAstroObjects` is a text file containing an astronomical source name per line. Non-valid names are ignored.

The result is a finding chart from SDSS DR9 as a JPEG file which is downloaded in the directory from which the `sdssDR9findingChart` script is called.

Installation
============

1. `wget https://github.com/juandesant/DownloadSDSSFindingCharts/archive/master.zip`
2. `unzip master.zip`
3. `cd DownloadSDSSFindingCharts-master/`
4. `python setup.py install`

The source code includes the `object.txt` file, with which you can test the script by typing

    sdssDR9findingChart objects.txt

The expected output will look like:

    Processing Sesame query for M31
    Processing Sesame query for HCG7d
    Processing Sesame query for m82
    Processing Sesame query for HCG89a
    Querying SDSS for coordinates 10.68470833 +41.26875000 (M31)
    Querying SDSS for coordinates 9.82830417 +0.89190833 (HCG7d)
    Querying SDSS for coordinates 320.00427083 -3.92211667 (HCG89a)
    Querying SDSS for coordinates 148.96745833 +69.68022222 (m82)
    Download of M31.jpg completed
    Processing Sesame query for HCG1
    Download of HCG89a.jpg completed
    Processing Sesame query for HCG2
    Querying SDSS for coordinates 6.50000000 +25.71666667 (HCG1)
    Download of m82.jpg completed
    Processing Sesame query for HCG92c
    Querying SDSS for coordinates 7.85000000 +8.44666667 (HCG2)
    Querying SDSS for coordinates 339.01483333 +33.97575000 (HCG92c)
    Download of HCG1.jpg completed
    Processing Sesame query for tontoElQueLoLea
    Error. Coordinates for tontoElQueLoLea not found in Sesame
    list index out of range
    Processing Sesame query for CIG 96
    Error. Coordinates for CIG 96 not found in Sesame
    list index out of range
    Processing Sesame query for CIG 3
    Error. Coordinates for CIG 3 not found in Sesame
    list index out of range
    Processing Sesame query for ngc4321
    Download of HCG2.jpg completed
    Querying SDSS for coordinates 185.72874583 +15.82238056 (ngc4321)
    Download of HCG92c.jpg completed
    Download of ngc4321.jpg completed
    Download of HCG7d.jpg completed

and the directory will contain the following files:

	$ ls -ln \*.jpg
	-rw-r--r--  1 501  20  103406 21 feb 22:40 CIG 3.jpg
	-rw-r--r--  1 501  20  122245 21 feb 22:40 CIG 96.jpg
	-rw-r--r--  1 501  20  102133 21 feb 22:39 HCG1.jpg
	-rw-r--r--  1 501  20  101813 21 feb 22:40 HCG2.jpg
	-rw-r--r--  1 501  20  118322 21 feb 22:39 HCG7d.jpg
	-rw-r--r--  1 501  20  113634 21 feb 22:39 HCG89a.jpg
	-rw-r--r--  1 501  20  120794 21 feb 22:40 HCG92c.jpg
	-rw-r--r--  1 501  20   22884 21 feb 22:39 M31.jpg
	-rw-r--r--  1 501  20  106942 21 feb 22:39 m82.jpg
	-rw-r--r--  1 501  20  109373 21 feb 22:40 ngc4321.jpg

Configuration
=============

Right now, the only configuration capabilities imply editing the script and manually modifying the `sdssParamsDict` dictionary.

For more information on which options are valid, see http://skyserver.sdss3.org/dr9/en/tools/chart/chart.asp

To do
=====

* Add help to the script
* Add configuration options corresponding to the chart using
* Add parallelisation, so that the tool can work faster, by querying multiple finding charts simultaneously

Aknowledgements
===============

This tool has been written withing the framework of the [AMIGA project](http://amiga.iaa.es/ "AMIGA : Analysis of the interstellar Medium of Isolated GAlaxies"), and with support from Spanish grants AYA2008-06181 and AYA2011-30491-C02.

Juande Santander Vela has a contract with CSIC (National Council for Scientific Research) in the JAE-Doc modality of the "Junta de Ampliación de Estudios" program, with funding from the European Social Fund.